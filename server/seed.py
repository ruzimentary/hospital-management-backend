from app import app
from models import db, Doctor, Department, Patient
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

    Doctor.query.delete()
    Department.query.delete()
    Patient.query.delete()


    doctors = []
    generated_emails = set()

    for _ in range(50):
        name = fake.first_name()
        domain = fake.free_email_domain()
        email = f'{name}@{domain}'

        # Ensure unique email
        while email in generated_emails:
            name = fake.first_name()
            domain = fake.free_email_domain()
            email = f'{name}@{domain}'

        generated_emails.add(email)
        
        speciality = fake.random_element(elements=specialties)
        doctors.append(Doctor(name=name, speciality=speciality, email=email))

    db.session.add_all(doctors)
    db.session.commit()

    departments = []

    for _ in range(10):
        department_name = fake.random_element(elements=list(departments_name))
        departments.append(Department(department_name=department_name))

    db.session.add_all(departments)
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


