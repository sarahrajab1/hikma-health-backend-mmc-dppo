from dataclasses import dataclass
from language_strings.language_string import LanguageString
from client_object import ClientObject
from datetime import datetime, date
from util import identity, parse_client_date, parse_client_timestamp


@dataclass
class Patient(ClientObject):
    id: str
    given_name: LanguageString
    surname: LanguageString
    date_of_birth: date
    sex: str
    country: LanguageString
    hometown: LanguageString
    locality: str
    city: str
    hai_village: str
    blok_no: str
    house_no: str
    occupation: str
    insurance: str
    private_insurance: str
    phone: str
    id_number: str
    record_number: str
    first_register_date: date
    edited_at: datetime

    def client_insert_values(self):
        return [self.id,
                self.format_string(self.given_name),
                self.format_string(self.surname),
                self.format_date(self.date_of_birth),
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.locality, 
                self.city, 
                self.hai_village, 
                self.blok_no, 
                self.house_no, 
                self.occupation, 
                self.insurance, 
                self.private_insurance, 
                self.phone, 
                self.id_number, 
                self.record_number, 
                self.format_date(self.first_register_date),
                self.format_ts(self.edited_at)]

    @classmethod
    def client_insert_sql(cls):
        return """INSERT INTO patients (id, given_name, surname, date_of_birth, sex, country, hometown, locality, city, hai_village, blok_no, house_no, occupation, insurance, private_insurance, phone, id_number, record_number, first_register_date, edited_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    def client_update_values(self):
        return [self.format_string(self.given_name),
                self.format_string(self.surname),
                self.format_date(self.date_of_birth),
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.locality, 
                self.city, 
                self.hai_village, 
                self.blok_no, 
                self.house_no, 
                self.occupation, 
                self.insurance, 
                self.private_insurance, 
                self.phone, 
                self.id_number, 
                self.record_number, 
                self.format_date(self.first_register_date),
                self.format_ts(self.edited_at),
                self.id]

    @classmethod
    def client_update_sql(cls):
        return """UPDATE patients SET given_name = ?, surname = ?, date_of_birth = ?, sex = ?, country = ?, hometown = ?, locality = ?, city = ?, hai_village = ?, blok_no = ?, house_no = ?, occupation = ?, insurance = ?, private_insurance = ?, phone = ?, id_number = ?, record_number = ?, first_register_date = ?, edited_at = ? WHERE id = ?"""
            

    def server_insert_values(self):
        return [self.id,
                self.format_string(self.given_name),
                self.format_string(self.surname),
                self.date_of_birth,
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.locality, 
                self.city, 
                self.hai_village, 
                self.blok_no, 
                self.house_no, 
                self.occupation, 
                self.insurance, 
                self.private_insurance, 
                self.phone, 
                self.id_number, 
                self.record_number, 
                self.first_register_date,
                self.edited_at]

    @classmethod
    def server_insert_sql(cls):
        return """INSERT INTO patients (id, given_name, surname, date_of_birth, sex, country, hometown, locality, city, hai_village, blok_no, house_no, occupation, insurance, private_insurance, phone, id_number, record_number, first_register_date, edited_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    def server_update_values(self):
        return [self.format_string(self.given_name),
                self.format_string(self.surname),
                self.date_of_birth,
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.locality, 
                self.city, 
                self.hai_village, 
                self.blok_no, 
                self.house_no, 
                self.occupation, 
                self.insurance, 
                self.private_insurance, 
                self.phone, 
                self.id_number, 
                self.record_number, 
                self.first_register_date,
                self.edited_at,
                self.id]

    @classmethod
    def server_update_sql(cls):
        return """UPDATE patients SET given_name = %s, surname = %s, date_of_birth = %s, sex = %s, country = %s, hometown = %s, locality = %s, city = %s, hai_village = %s, blok_no = %s, house_no = %s, occupation = %s, insurance = %s, private_insurance = %s, phone = %s, id_number = %s, record_number = %s, first_register_date = %s, edited_at = %s WHERE id = %s"""


    @classmethod
    def db_columns_from_server(cls):
        return [('id', lambda s: s.replace('-', '')),
                ('given_name', cls.make_language_string),
                ('surname', cls.make_language_string),
                ('date_of_birth', identity),
                ('sex', identity),
                ('country', cls.make_language_string),
                ('hometown', cls.make_language_string),
                ('locality', identity),
                ('city', identity),
                ('hai_village', identity),
                ('blok_no', identity),
                ('house_no', identity),
                ('occupation', identity),
                ('insurance', identity),
                ('private_insurance', identity),
                ('phone', identity),
                ('id_number', identity),
                ('record_number', identity),
                ('first_register_date', identity),
                ('edited_at', identity)]

    @classmethod
    def db_columns_from_client(cls):
        return [('id', identity),
                ('given_name', cls.make_language_string),
                ('surname', cls.make_language_string),
                ('date_of_birth', parse_client_date),
                ('sex', identity),
                ('country', cls.make_language_string),
                ('hometown', cls.make_language_string),
                ('locality', identity),
                ('city', identity),
                ('hai_village', identity),
                ('blok_no', identity),
                ('house_no', identity),
                ('occupation', identity),
                ('insurance', identity),
                ('private_insurance', identity),
                ('phone', identity),
                ('id_number', identity),
                ('record_number', identity),
                ('first_register_date', identity),
                ('edited_at', parse_client_timestamp)]

    @classmethod
    def table_name(cls):
        return "patients"

    @classmethod
    def from_db_row(cls, db_row):
        id, given_name, surname, date_of_birth, sex, country, hometown, locality, city, hai_village, blok_no, house_no, occupation, insurance, private_insurance, phone, id_number, record_number, first_register_date, edited_at = db_row
        return cls(id, LanguageString.from_id(given_name), LanguageString.from_id(surname), date_of_birth, sex, LanguageString.from_id(country), LanguageString.from_id(hometown), locality, city, hai_village, blok_no, house_no, occupation, insurance, private_insurance, phone, id_number, record_number, first_register_date, edited_at)    

    def to_dict(self):
        return {
            'id': self.id,
            'given_name': self.given_name.to_dict() if self.given_name is not None else None,
            'surname': self.surname.to_dict() if self.surname is not None else None,
            'date_of_birth': self.date_of_birth,
            'sex': self.sex,
            'country': self.country.to_dict() if self.country is not None else None,
            'hometown': self.hometown.to_dict() if self.hometown is not None else None,
            'locality' :self.locality, 
            'city' :self.city, 
            'hai_village': self.hai_village, 
            'blok_no': self.blok_no, 
            'house_no': self.house_no, 
            'occupation': self.occupation, 
            'insurance': self.insurance, 
            'private_insurance': self.private_insurance, 
            'phone': self.phone, 
            'id_number': self.id_number, 
            'record_number': self.record_number, 
            'first_register_date': self.first_register_date,
            'edited_at': self.edited_at
        }