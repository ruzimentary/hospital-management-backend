from app import app
from models import db, Doctor, Department
from faker import Faker

with app.app_context():
    fake = Faker()
    specialties = [
        "Cardiology", "Dermatology", "Endocrinology", "Gastroenterology",
        "Hematology", "Nephrology", "Neurology", "Oncology", "Ophthalmology",
        "Orthopedics", "Pediatrics", "Psychiatry", "Radiology", "Surgery"
    ]

    Doctor.query.delete()

    doctors = []
    generated_emails = set()

    for _ in range(100):
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

