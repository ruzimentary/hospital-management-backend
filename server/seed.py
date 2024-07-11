from app import app
from models import db, Doctor, Department, Patient, Appointment, MedicalRecord, Medication
from faker import Faker
from datetime import date, datetime

with app.app_context():
    fake = Faker()
    specialties = [
        "Cardiology", "Dermatology", "Endocrinology", "Gastroenterology",
        "Hematology", "Nephrology", "Neurology", "Oncology", "Ophthalmology",
        "Orthopedics", "Pediatrics", "Psychiatry", "Radiology", "Surgery"
    ]

    departments_name = {"Cardiology Department","Dermatology Department","Endocrinology Department", "Gastroenterology Department", "Hematology Department", "Nephrology Department", "Neurology Department", "Oncology Department", "Ophthalmology Department", "Orthopedics Department", "Pediatrics Department", "Psychiatry Department", "Radiology Department", "Surgery Department"
    }

    medications_name = {  "Amoxicillin", "Ibuprofen", "Lisinopril", "Metformin", "Simvastatin", "Omeprazole", "Levothyroxine", "Azithromycin", "Amlodipine", "Losartan", "Hydrochlorothiazide", "Atorvastatin", "Gabapentin", "Zolpidem", "Metoprolol", "Clopidogrel", "Montelukast", "Furosemide", "Pantoprazole", "Escitalopram", "Citalopram", "Sertraline", "Prednisone", "Tramadol", "Cyclobenzaprine", "Ciprofloxacin", "Doxycycline", "Meloxicam", "Oxycodone", "Hydroxychloroquine"}

    specialty_department_map = {
    "Cardiology": "Cardiology Department",
    "Dermatology": "Dermatology Department",
    "Endocrinology": "Endocrinology Department",
    "Gastroenterology": "Gastroenterology Department",
    "Hematology": "Hematology Department",
    "Nephrology": "Nephrology Department",
    "Neurology": "Neurology Department",
    "Oncology": "Oncology Department",
    "Ophthalmology": "Ophthalmology Department",
    "Orthopedics": "Orthopedics Department",
    "Pediatrics": "Pediatrics Department",
    "Psychiatry": "Psychiatry Department",
    "Radiology": "Radiology Department",
    "Surgery": "Surgery Department"
}


    Doctor.query.delete()
    Department.query.delete()
    Patient.query.delete()
    Appointment.query.delete()
    MedicalRecord.query.delete()
    Medication.query.delete()

    departments = []

    for _ in range(10):
        department_name = fake.random_element(elements=list(departments_name))
        departments.append(Department(department_name=department_name))

    db.session.add_all(departments)
    db.session.commit()

    doctors = []
    generated_emails = set()

    for _ in range(50):
        name = fake.first_name()
        domain = fake.free_email_domain()
        email = f'{name.lower()}@{domain}'

        while email in generated_emails:
            name = fake.first_name()
            domain = fake.free_email_domain()
            email = f'{name.lower()}@{domain}'

        generated_emails.add(email)
        
        speciality = fake.random_element(elements=specialties)
        department_name = specialty_department_map.get(speciality)
        department = Department.query.filter_by(department_name=department_name).first()

        new_doctor = Doctor(name=name, speciality=speciality, email=email, department=department)
        db.session.add(new_doctor)
        doctors.append(new_doctor)

    db.session.commit()


    patients = []

    for _ in range(100):
        name = fake.first_name()
        birth_date = fake.date_of_birth(minimum_age=0, maximum_age=100)
        age = date.today().year - birth_date.year
        gender = fake.random_element(elements=('Male', 'Female'))
        created_date = datetime.strptime(fake.date(), '%Y-%m-%d').date()

        patients.append(Patient(name=name, age=age, gender=gender, date=created_date))

    db.session.add_all(patients)
    db.session.commit()

    appointments = []

    for _ in range(200):
        doctor = fake.random_element(elements=doctors)
        patient = fake.random_element(elements=patients)
        appointment_date = fake.date_between(start_date='-1y', end_date='+1y')

        appointments.append(Appointment(doctor_id=doctor.id, patient_id=patient.id, appointment_date=appointment_date))

    db.session.add_all(appointments)
    db.session.commit()

    medications = []

    for _ in range(30):
        medication_name = fake.random_element(elements=medications_name)
        dosage = f"{fake.random_int(min=1, max=500)} mg"

        medications.append(Medication(medication_name=medication_name, dosage=dosage))

    db.session.add_all(medications)
    db.session.commit()

    medicalrecords = []

    import random
    patient_ids = [patient.id for patient in Patient.query.all()]
    medication_ids = [medication.id for medication in Medication.query.all()]

    for _ in range(100):
        patient_id = random.choice(patient_ids)
        medication_id = random.choice(medication_ids)
        diagnosis = fake.sentence(nb_words=6)

        medicalrecords.append(MedicalRecord(patient_id=patient_id, medication_id=medication_id, diagnosis=diagnosis))

    db.session.add_all(medicalrecords)
    db.session.commit()