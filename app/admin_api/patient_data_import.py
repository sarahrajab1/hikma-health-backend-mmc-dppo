from dataclasses import dataclass

COLUMNS = [
    'camp',
    'visit_date',
    'visit_type',
    'clinic_estate',
    'clinic_city',
    'clinic_name',
    'first_name',
    'surname',
    'date_of_birth',
    'age',
    'gender',
    'hometown',
    'home_country',
    'locality',
    'city',
    'hai_village',
    'blok_no',
    'house_no',
    'occupation',
    'insurance',
    'private_insurance',
    'phone',
    'id_number',
    'record_number',
    'first_register_date',
    'doctor',
    # medical hx
    'allergies',
    'surgery_hx',
    'chronic_conditions',
    'current_medications',
    'vaccinations',
    # complaint
    'complaint',
    # vitals
    'height',
    'weight',
    'bmi',
    'waist_circumference',
    'blood_pressure',
    'pulse',
    # examination
    'examination_complaint',
    'active_conditions',
    'illness_history',
    # medicines_1 
    # 'medication_1',
    # 'type_1',
    # 'dosage_1',
    # 'days_1',
    # # medicines_2
    # 'medication_2',
    # 'type_2',
    # 'dosage_2',
    # 'days_2',
    # # medicines_3
    # 'medication_3',
    # 'type_3',
    # 'dosage_3',
    # 'days_3',
    # # medicines_4
    # 'medication_4',
    # 'type_4',
    # 'dosage_4',
    # 'days_4',
    # # medicines_5
    # 'medication_5',
    # 'type_5',
    # 'dosage_5',
    # 'days_5',
    # medicines
    'on_statin',
    'statin_name_dose',
    'diabetes',
    'htn',
    'non_diabetes',
    'other_medicines',
    # physiotherapy
    'previous_treatment',
    'complaint_p',
    'findings',
    'treatment_plan',
    'treatment_session',
    'recommendations',
    'referral',
    'dental_treatment',
    'notes',
    'covid_19_result',
    # deprecated
    'examination_d',
    'medical_hx_d',
    'treatment_d',
    'diagnosis_d',
    'medicine_dispensed_d',
    'prescriptions_d',
    'allergies_d',
    # DM History
    'diagnosis_age',
    'dm_duration',
    'diabetes_type',
    'management',
    'family_history',
    'smoker',
    'alcohol',
    'cardiac_problem',
    'hf_sign',
    'hypertension',
    'renal_problem',
    'eye_problem',
    'hypoglycemia_requiring',
    'dka',
    'myocardial',
    'cerebral_stroke',
    'limb_amputation',
    'erectile_dysfunction',
    'retinal_examination',
    # Clinical Examination
    'respiratory_system',
    'respiratory_system_note',
    'cvs',
    'cvs_note',
    'abdomen',
    'abdomen_note',
    'musculoskeletal',
    'musculoskeletal_note',
    'cns',
    'cns_note',
    # foot examination
    'rt_vibration',
    'rt_monofilament',
    'rt_distal_pulse',
    'rt_dorsalis_pulse',
    'rt_posterior_pulse',
    'left_vibration',
    'left_monofilament',
    'left_distal_pulse',
    'left_dorsalis_pulse',
    'left_posterior_pulse',
    # lab investigation
    'hb_a1c',
    'hb_a1c_value',
    'fating_glucose',
    'fating_glucose_value',
    'random_glucose',
    'random_glucose_value',
    'post_meal_glucose',
    'post_meal_glucose_value',
    'creatinine',
    'creatinine_value',
    'egfr',
    'egfr_value',
    'total_cholesterol',
    'total_cholesterol_value',
    'ldl_cholesterol',
    'ldl_cholesterol_value',
    'hdl',
    'hdl_value',
    'tg',
    'tg_value',
    'sodium',
    'sodium_value',
    'potassium',
    'potassium_value',
    'haemoglobin',
    'haemoglobin_value',
    'urinary_acr',
    'urinary_acr_value',
    'dipstick_protein',
    'dipstick_protein_value',
    'urine_protein',
    'urine_protein_value',
    'urine_sugar',
    'urine_sugar_value',
    'urine_microalbuminuria',
    'urine_microalbuminuria_value',
    'urine_ketones',
    'urine_ketones_value',
    'ecg',
    'ecg_value',
    'other_investigations',
    # Ophthalmology Examination
    'rt_dilated_fundoscopy',
    'rt_ophthalmologist',
    'rt_retinal_camera',
    'rt_findings',
    'left_dilated_fundoscopy',
    'left_ophthalmologist',
    'left_retinal_camera',
    'left_findings',
    # Endocrinologist Cases
    'indications',
    'feedback',
    # Referrals
    'diabetic_educator',
    'dietitian',
    'ophthalmologist',
    'foot_care_clinic',
    'social_services',
    'psychologist',
    'referral_date',
    # Diabeted Education
    'visit_note'
]

@dataclass
class PatientDataRow:
    camp: str = None
    visit_date: str = None
    visit_type: str = None
    clinic_estate: str = None
    clinic_city: str = None
    clinic_name: str = None
    first_name: str = None
    surname: str = None
    date_of_birth: str = None
    age: str = None
    gender: str = None
    hometown: str = None
    home_country: str = None
    locality: str = None
    city: str = None
    hai_village: str = None
    blok_no: str = None
    house_no: str = None
    occupation: str = None
    insurance: str = None
    private_insurance: str = None
    phone: str = None
    id_number: str = None
    record_number: str = None
    first_register_date: str = None
    doctor: str = None
    allergies: str = None
    surgery_hx: str = None
    chronic_conditions: str = None
    current_medications: str = None
    vaccinations: str = None
    complaint: str = None
    height: str = None
    weight: str = None
    bmi: str = None
    waist_circumference: str = None
    blood_pressure: str = None
    pulse: str = None
    examination_complaint: str = None
    active_conditions: str = None
    illness_history: str = None
    examination: str = None
    general_observations: str = None
    diagnosis: str = None
    treatment: str = None
    covid_19: str = None
    referral: str = None
    medication_1: str = None
    type_1: str = None
    dosage_1: str = None
    days_1: str = None
    medication_2: str = None
    type_2: str = None
    dosage_2: str = None
    days_2: str = None
    medication_3: str = None
    type_3: str = None
    dosage_3: str = None
    days_3: str = None
    medication_4: str = None
    type_4: str = None
    dosage_4: str = None
    days_4: str = None
    medication_5: str = None
    type_5: str = None
    dosage_5: str = None
    days_5: str = None
    previous_treatment: str = None
    complaint_p: str = None
    findings: str = None
    treatment_plan: str = None
    treatment_session: str = None
    recommendations: str = None
    referral: str = None
    dental_treatment: str = None
    notes: str = None
    covid_19_result: str = None
    examination_d: str = None
    medical_hx_d: str = None
    treatment_d: str = None
    diagnosis_d: str = None
    medicine_dispensed_d: str = None
    prescriptions_d: str = None
    allergies_d: str = None
    # DM History
    diagnosis_age: str = None
    dm_duration: str = None
    diabetes_type: str = None
    management: str = None
    family_history: str = None
    smoker: str = None
    alcohol: str = None
    cardiac_problem: str = None
    hf_sign: str = None
    hypertension: str = None
    renal_problem: str = None
    eye_problem: str = None
    hypoglycemia_requiring: str = None
    dka: str = None
    myocardial: str = None
    cerebral_stroke: str = None
    limb_amputation: str = None
    erectile_dysfunction: str = None
    retinal_examination: str = None
    # Clinical Examination
    respiratory_system: str = None
    respiratory_system_note: str = None
    cvs: str = None
    cvs_note: str = None
    abdomen: str = None
    abdomen_note: str = None
    musculoskeletal: str = None
    musculoskeletal_note: str = None
    cns: str = None
    cns_note: str = None
    # medicines
    on_statin: str = None
    statin_name_dose: str = None
    diabetes: str = None
    htn: str = None
    non_diabetes: str = None
    other_medicines: str = None
    # foot examination
    rt_vibration: str = None
    rt_monofilament: str = None
    rt_distal_pulse: str = None
    rt_dorsalis_pulse: str = None
    rt_posterior_pulse: str = None
    left_vibration: str = None
    left_monofilament: str = None
    left_distal_pulse: str = None
    left_dorsalis_pulse: str = None
    left_posterior_pulse: str = None
    # lab investigation
    hb_a1c: str = None
    hb_a1c_value: str = None
    fating_glucose: str = None
    fating_glucose_value: str = None
    random_glucose: str = None
    random_glucose_value: str = None
    post_meal_glucose: str = None
    post_meal_glucose_value: str = None
    creatinine: str = None
    creatinine_value: str = None
    egfr: str = None
    egfr_value: str = None
    total_cholesterol: str = None
    total_cholesterol_value: str = None
    ldl_cholesterol: str = None
    ldl_cholesterol_value: str = None
    hdl: str = None
    hdl_value: str = None
    tg: str = None
    tg_value: str = None
    sodium: str = None
    sodium_value: str = None
    potassium: str = None
    potassium_value: str = None
    haemoglobin: str = None
    haemoglobin_value: str = None
    urinary_acr: str = None
    urinary_acr_value: str = None
    dipstick_protein: str = None
    dipstick_protein_value: str = None
    urine_protein: str = None
    urine_protein_value: str = None
    urine_sugar: str = None
    urine_sugar_value: str = None
    urine_microalbuminuria: str = None
    urine_microalbuminuria_value: str = None
    urine_ketones: str = None
    urine_ketones_value: str = None
    ecg: str = None
    ecg_value: str = None
    other_investigations: str = None
    # Ophthalmology Examination
    rt_dilated_fundoscopy: str = None
    rt_ophthalmologist: str = None
    rt_retinal_camera: str = None
    rt_findings: str = None
    left_dilated_fundoscopy: str = None
    left_ophthalmologist: str = None
    left_retinal_camera: str = None
    left_findings: str = None
    # Endocrinologist Cases
    indications: str = None
    feedback: str = None
    # Referrals
    diabetic_educator: str = None
    dietitian: str = None
    ophthalmologist: str = None
    foot_care_clinic: str = None
    social_services: str = None
    psychologist: str = None
    referral_date: str = None
    # Diabetes Education
    visit_note: str = None



# COLUMN_TYPES = [str, None, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, float, str,
#                 float, float, float, float, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str,
#                 str, str]


# class PatientDataImporter:
#     def __init__(self, data_file: FileStorage):
#         self.data_filename = self._write_file_to_tempfile(data_file)

#     def run(self):
#         all_rows = [self._parse_row(row) for row in self.iter_data_rows()]
#         print('Creating patients...')
#         self._create_patients(all_rows)
#         print('Creating visits...')
#         self._create_visits(all_rows)

#     def _parse_row(self, row):
#         if len(row) != 41:
#             raise WebError('All data rows must have exactly 41 data points.', 400)
#         values = [self._parse_cell(value, formatter) for value, formatter in zip(row, COLUMN_TYPES)]
#         return PatientDataRow(**dict(zip(COLUMNS, values)))

#     def _parse_cell(self, cell, formatter):
#         if cell == 'Nil' or cell is None:
#             return None
#         if formatter is None:
#             return cell
#         return formatter(cell)

#     @staticmethod
#     def _write_file_to_tempfile(data_file: FileStorage):
#         handle = NamedTemporaryFile('wb', delete=False, suffix='.xlsx')
#         data_file.save(handle)
#         handle.close()
#         print('Upload written to', handle.name)
#         return handle.name

#     def iter_data_rows(self):
#         wb = load_workbook(self.data_filename)
#         ws = wb.active
#         for idx, row in enumerate(ws.iter_rows(min_row=3, max_col=41, values_only=True)):
#             if all(x is None for x in row):
#                 continue
#             yield row

#     def _create_patients(self, rows: Iterable[PatientDataRow]):
#         for patient_data in set(map(lambda r: (r.first_name, r.surname, r.gender, r.home_country, r.age), rows)):
#             first_name, surname, gender, home_country, age = patient_data
#             if not patient_from_key_data(first_name, surname, home_country, self._parse_sex(gender)):
#                 self._create_patient(first_name, surname, home_country, gender, age)

#     def _create_patient(self, given_name, surname, home_country, sex, age):
#         given_name_ls = LanguageString(id=str(uuid.uuid4()), content_by_language={'en': given_name})
#         surname_ls = LanguageString(id=str(uuid.uuid4()), content_by_language={'en': surname})
#         inferred_dob = self._infer_dob(age)
#         patient = Patient(
#             id=str(uuid.uuid4()),
#             edited_at=datetime.now(),
#             given_name=given_name_ls,
#             surname=surname_ls,
#             date_of_birth=inferred_dob,
#             sex=self._parse_sex(sex),
#             country=LanguageString(id=str(uuid.uuid4()), content_by_language={'en': home_country}),
#             phone=None,
#             hometown=None
#         )
#         add_patient(patient)

#     @staticmethod
#     def _parse_sex(sex_str):
#         if sex_str is None:
#             return None
#         elif 'm' in sex_str.lower():
#             return 'M'
#         elif 'f' in sex_str.lower():
#             return 'F'
#         else:
#             return None

#     def _infer_dob(self, age_string):
#         try:
#             int_prefix = int(''.join(itertools.takewhile(str.isnumeric, age_string)))
#             today = date.today()
#             if 'months' in age_string:
#                 return today - timedelta(days=30 * int_prefix)
#             elif 'weeks' in age_string:
#                 return today - timedelta(weeks=int_prefix)
#             elif 'days' in age_string:
#                 return today - timedelta(days=int_prefix)
#             else:
#                 # Assume years if no unit is specified
#                 return today - timedelta(days=365 * int_prefix)
#         except (ValueError, TypeError):
#             return date(1900, 1, 1)

#     @staticmethod
#     def _parse_date(date_str):
#         if isinstance(date_str, date) or isinstance(date_str, datetime):
#             return date_str
#         try:
#             dt = pd.to_datetime(date_str, dayfirst=True).to_pydatetime()
#             return date(year=dt.year, month=dt.month, day=dt.day)
#         except dateutil.parser._parser.ParserError:
#             return None

#     def _create_visits(self, rows: Iterable[PatientDataRow]):
#         for row in rows:
#             patient_id = patient_from_key_data(row.first_name, row.surname, row.home_country, self._parse_sex(row.gender))
#             if not patient_id:
#                 print('Warning: unknown patient; skipping.')
#                 continue
#             visit_date = self._parse_date(row.visit_date)
#             visit_id, visit_timestamp = first_visit_by_patient_and_date(patient_id, visit_date)

#             # TODO: The data import format does not currently specify a clinic. Since
#             # current Hikma instances are single clinic anyway, just get the most common
#             # clinic (in case there is a demo one with few if any visits) and use that.
#             clinic_id = get_most_common_clinic()

#             # TODO: The data import format does not currently specify a provider in a format
#             # that we can use. So for now, use a per-instance default provider that is set via
#             # environment variable.
#             provider_id = DEFAULT_PROVIDER_ID_FOR_IMPORT

#             if visit_id is None:
#                 visit_id = str(uuid.uuid4())
#                 visit_timestamp = datetime.combine(visit_date, datetime.min.time())
#                 visit = Visit(
#                     id=visit_id,
#                     patient_id=patient_id,
#                     edited_at=datetime.now(),
#                     clinic_id=clinic_id,
#                     provider_id=provider_id,
#                     check_in_timestamp=visit_timestamp
#                 )
#                 add_visit(visit)

#                 # Until we implement full deletion, only add visit the first time it is seen.
#                 self._update_events(patient_id, visit_id, visit_timestamp, row)

#     def _update_events(self, patient_id: str, visit_id: str, visit_timestamp: datetime, row: PatientDataRow):
#         # TODO: This will need to be replaced with a mode of deletion that persists through synchronization.
#         # clear_all_events(visit_id)
#         if row.allergies:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Allergies', row.allergies)
#         if any([row.dispensed_medicine_1, row.dispensed_medicine_2,
#                 row.dispensed_medicine_3, row.dispensed_medicine_4]):
#             self._add_dispensed_medicine_event(patient_id, visit_id, visit_timestamp, row)
#         if row.presenting_complaint:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Complaint', row.presenting_complaint)
#         if any([row.heart_rate, row.blood_pressure, row.o2_sats,
#                 row.respiratory_rate, row.temperature, row.blood_glucose]):
#             self._add_vitals_event(patient_id, visit_id, visit_timestamp, row)
#         if row.examination:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Examination', row.examination)
#         if row.diagnosis:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Diagnosis', row.diagnosis)
#         if row.treatment:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Treatment', row.treatment)
#         if row.prescription:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Prescriptions', row.prescription)
#         if row.notes:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Notes', row.notes)
#         if row.camp:
#             self._add_text_event(patient_id, visit_id, visit_timestamp, 'Camp', row.camp)

#     def _add_text_event(self, patient_id: str, visit_id: str, visit_timestamp: datetime,
#                         event_type: str, event_metadata: str):
#         event = Event(
#             id=str(uuid.uuid4()),
#             patient_id=patient_id,
#             visit_id=visit_id,
#             event_type=event_type,
#             event_timestamp=visit_timestamp,
#             event_metadata=event_metadata,
#             edited_at=datetime.now(),
#         )
#         add_event(event)

#     def _add_dispensed_medicine_event(self,  patient_id: str, visit_id: str, visit_timestamp: datetime, row: PatientDataRow):
#         data = [
#             (row.dispensed_medicine_1, row.dispensed_medicine_quantity_1),
#             (row.dispensed_medicine_2, row.dispensed_medicine_quantity_2),
#             (row.dispensed_medicine_3, row.dispensed_medicine_quantity_3),
#             (row.dispensed_medicine_4, row.dispensed_medicine_quantity_4),
#         ]
#         content = '\n'.join([': '.join(r) for r in data if all(r)])
#         event = Event(
#             id=str(uuid.uuid4()),
#             patient_id=patient_id,
#             visit_id=visit_id,
#             event_type='Medicine Dispensed',
#             event_timestamp=visit_timestamp,
#             event_metadata=content,
#             edited_at=datetime.now(),
#         )
#         add_event(event)

#     def _add_vitals_event(self,  patient_id: str, visit_id: str, visit_timestamp: datetime, row: PatientDataRow):
#         try:
#             diastolic, systolic = row.blood_pressure.split('/')
#         except (ValueError, AttributeError):
#             diastolic = None
#             systolic = None

#         data = {
#             'heartRate': as_string(row.heart_rate),
#             'systolic': as_string(systolic),
#             'diastolic': as_string(diastolic),
#             'sats': as_string(row.o2_sats),
#             'temp': as_string(row.temperature),
#             'respiratoryRate': as_string(row.respiratory_rate),
#             'bloodGlucose': as_string(row.blood_glucose)
#         }

#         event = Event(
#             id=str(uuid.uuid4()),
#             patient_id=patient_id,
#             visit_id=visit_id,
#             event_type='Vitals',
#             event_timestamp=visit_timestamp,
#             event_metadata=json.dumps(data),
#             edited_at=datetime.now(),
#         )
#         add_event(event)
