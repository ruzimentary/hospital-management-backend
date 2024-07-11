from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime, timezone

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Doctor(db.Model, SerializerMixin):
    __tablename__ = 'Doctors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    speciality = db.Column(db.String(50), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))

    def __repr__(self) -> str:
        return {self.name}

class Department(db.Model, SerializerMixin):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return {self.department_name}
    
class Patient(db.Model, SerializerMixin):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(2), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return {self.name}
    
class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String(50), nullable=False)
    patient_name = db.Column(db.String(50), nullable=False)
    appointment_date = db.Column(db.Date, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return {self.appointment_date}
    
class Medication(db.Model, SerializerMixin):
    __tablename__ = 'medications'

    id = db.Column(db.Integer, primary_key=True)
    medication_name = db.Column(db.String(50), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"<Medication(name={self.medication_name}, dosage={self.dosage})>"
    
class Medicalrecords(db.Model, SerializerMixin):
    __tablename__ = 'medicalrecords'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.id'))
    dosage = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f'{self.dosage}'

