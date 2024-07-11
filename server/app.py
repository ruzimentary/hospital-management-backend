from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Doctor, Department, Patient, Appointment,  Medication, Medicalrecords

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Welcome to the system'

@app.route('/doctors', methods=['GET'])
def get_all_doctors():
    doctors = Doctor.query.all()
    return jsonify([doctor.to_dict() for doctor in doctors])

@app.route('/departments', methods=['GET'])
def get_all_departments():
    departments = Department.query.all()
    return jsonify([department.to_dict() for department in departments])

@app.route('/patients', methods=['GET'])
def get_all_patients():
    patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])

@app.route('/appointments', methods=['GET'])
def get_all_appointments():
    appointments = Appointment.query.all()
    return jsonify([appointment.to_dict() for appointment in appointments])

@app.route('/medications', methods=['GET'])
def get_all_medications():
    medications = Medication.query.all()
    return jsonify([medication.to_dict() for medication in medications])

@app.route('/medicalrecords', methods=['GET'])
def get_all_medicalrecords():
    medications = Medicalrecords.query.all()
    return jsonify([medication.to_dict() for medication in medications])

if __name__ == "__main__":
    app.run(port=5555, debug=True)