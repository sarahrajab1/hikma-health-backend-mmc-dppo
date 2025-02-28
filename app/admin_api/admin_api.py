from flask import Blueprint, request, jsonify, send_file
from web_util import assert_data_has_keys, admin_authenticated
from web_errors import WebError
from users.user import User
from patients.patient import Patient
from patients.data_access import all_patient_data, search_patients, delete_all_patients_data
from users.data_access import all_user_data, add_user, delete_user_by_id, user_data_by_email
from language_strings.language_string import LanguageString
from admin_api.patient_data_export import most_recent_export
from admin_api.single_patient_data_export import single_patient_export
from admin_api.patient_data_export import PatientDataExporter

import uuid
import bcrypt
import psycopg2.errors


from clinics.clinic import Clinic
from clinics.data_access import add_clinic, all_clinic_data
import uuid
from datetime import datetime

from config import EXPORTS_STORAGE_BUCKET
from google.cloud import storage

admin_api = Blueprint('admin_api', __name__, url_prefix='/admin_api')

@admin_api.route('/add_clinic', methods=['GET'])
def add_demo_clinic():
    clinic = Clinic(id=str(uuid.uuid4()), edited_at=datetime.now(), name=LanguageString(
    id=str(uuid.uuid4()), content_by_language={
        'en': 'EMA'
    }))
    add_clinic(clinic)

    return jsonify({'clinic': "EMA"})

@admin_api.route('/empty_db', methods=['GET'])
@admin_authenticated
def empty_db(_admin_user):
    delete_all_patients_data()

    return jsonify({'status': "Done"})

@admin_api.route('/list_clinics', methods=['GET'])
def list_clinics():
    all_clinics = [Clinic.from_db_row(r).to_dict() for r in all_clinic_data()]
    return jsonify({'clinics': all_clinics})

@admin_api.route('/login', methods=['POST'])
def login():
    params = assert_data_has_keys(request, {'email', 'password'})
    user = User.authenticate(params['email'], params['password'])
    token = user.create_token()
    return jsonify({'token': token})


@admin_api.route('/logout', methods=['POST'])
@admin_authenticated
def logout(admin_user: User):
    admin_user.logout()
    return jsonify({'message': 'OK'})


@admin_api.route('/all_users', methods=['GET'])
@admin_authenticated
def get_all_users(_admin_user):
    all_users = [User.from_db_row(r).to_dict() for r in all_user_data()]
    return jsonify({'users': all_users})


@admin_api.route('/user', methods=['POST'])
@admin_authenticated
def create_user(_admin_user):
    params = assert_data_has_keys(request, {'email', 'password', 'name', 'role'})
    if params['role'] not in ['admin', 'provider']:
        raise WebError('Role must be either "admin" or "provider"', 400)

    id = str(uuid.uuid4())
    language = params.get('language', 'en')
    name_str = LanguageString(id=str(uuid.uuid4()), content_by_language={language: params['name']})
    hashed_password = bcrypt.hashpw(params['password'].encode(), bcrypt.gensalt()).decode()
    user = User(id, name_str, params['role'], params['email'], hashed_password)
    try:
        add_user(user)
    except psycopg2.errors.UniqueViolation:
        raise WebError('User already exists', 409)

    all_users = [User.from_db_row(r).to_dict() for r in all_user_data()]
    return jsonify({'users': all_users})


@admin_api.route('/user', methods=['DELETE'])
@admin_authenticated
def delete_user(_admin_user):
    params = assert_data_has_keys(request, {'email'})
    user = User.from_db_row(user_data_by_email(params['email']))
    delete_user_by_id(user.id)
    all_users = [User.from_db_row(r).to_dict() for r in all_user_data()]
    return jsonify({'users': all_users})


@admin_api.route('/change_password', methods=['POST'])
@admin_authenticated
def change_password(_admin_user):
    params = assert_data_has_keys(request, {'email', 'new_password'})
    user = User.from_db_row(user_data_by_email(params['email']))
    user.reset_password(params['new_password'])
    return jsonify({'message': 'ok'})


# @admin_api.route('/upload', methods=['POST'])
# @admin_authenticated
# def upload_patient_data(_admin_user):
#     if len(request.files) == 0:
#         raise WebError('Files must be present', 400)

#     importer = PatientDataImporter(request.files['file'])
#     importer.run()
#     return jsonify({'message': 'OK'})

@admin_api.route('/run-export', methods=['GET'])
@admin_authenticated
def run_export(_admin_user):
    storage_client = storage.Client()

    exporter = PatientDataExporter()
    local_filename = exporter.run()

    bucket = storage_client.bucket(EXPORTS_STORAGE_BUCKET)
    base_name = datetime.utcnow().isoformat() + '.xlsx'
    blob = bucket.blob(base_name)
    print(f'Uploading {base_name} to GCS bucket {EXPORTS_STORAGE_BUCKET}...')
    blob.upload_from_filename(local_filename)

@admin_api.route('/export', methods=['POST'])
@admin_authenticated
def export_all_data(_admin_user):
    export_filename = most_recent_export()
    return send_file(export_filename, attachment_filename='hikma_export.xlsx')


@admin_api.route('/all_patients', methods=['GET'])
@admin_authenticated
def get_all_patients(_admin_user):
    all_patients = [Patient.from_db_row(r).to_dict() for r in all_patient_data()]
    return jsonify({'patients': all_patients})


@admin_api.route('/search_patients', methods=['POST'])
@admin_authenticated
def search(_admin_user):
    params = assert_data_has_keys(request, {'given_name', 'surname', 'country', 'hometown', 'clinic_city', 'clinic_name'})
    patient = [Patient.from_db_row(r).to_dict() for r in search_patients(params['given_name'], params['surname'], params['country'], params['hometown'], params['clinic_city'], params['clinic_name'])]
    return jsonify({'patient': patient})
        

@admin_api.route('/export_patient', methods=['POST'])
@admin_authenticated
def export_patient_data(_admin_user):
    params = assert_data_has_keys(request, {'patient_id'})
    export_filename = single_patient_export(params['patient_id'])
    return send_file(export_filename, attachment_filename='hikma_patient_export.xlsx')
