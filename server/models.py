from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'doctors'
    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    speciality = db.Column(db.String(50), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    department = db.relationship('Department', back_populates='doctors')
    appointments = db.relationship('Appointment', back_populates='doctor')

    serialize_rules = ('-appointments.doctor', '-department.doctors')

    def __repr__(self) -> str:
        return {self.name}

class Department(db.Model, SerializerMixin):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50), nullable=False)

    doctors = db.relationship('Doctor', back_populates='department')

    serialize_rules = ('-doctors.department',)

    def __repr__(self) -> str:
        return {self.department_name}
    
class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(2), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=datetime.now(timezone.utc))

    appointments = db.relationship('Appointment', back_populates='patient')
    medical_records = db.relationship('MedicalRecord', back_populates='patient') 

    serialize_rules = ('-appointments.patient', '-medical_records.patient')

    def __repr__(self) -> str:
        return {self.name}
    
class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id')) 
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))  
    appointment_date = db.Column(db.Date, default=datetime.now(timezone.utc))

    doctor = db.relationship('Doctor', back_populates='appointments')
    patient = db.relationship('Patient', back_populates='appointments') 

    serialize_rules = ('-doctor.appointments', '-patient.appointments')

    def __repr__(self) -> str:
        return {self.appointment_date}
    
class Medication(db.Model, SerializerMixin):
    __tablename__ = 'medications'

    id = db.Column(db.Integer, primary_key=True)
    medication_name = db.Column(db.String(50), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)

    medical_records = db.relationship('MedicalRecord', back_populates='medication')

    serialize_rules = ('-medical_records.medication',)

    def __repr__(self) -> str:
        return f"<Medication(name={self.medication_name}, dosage={self.dosage})>"
    
class MedicalRecord(db.Model, SerializerMixin):
    __tablename__ = 'medicalrecords'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'))
    diagnosis = db.Column(db.String(200), nullable=False) 

    patient = db.relationship('Patient', back_populates='medical_records')  
    medication = db.relationship('Medication', back_populates='medical_records')  

    serialize_rules = ('-patient.medical_records', '-medication.medical_records')

    def __repr__(self) -> str:
        return f'{self.dosage}'

