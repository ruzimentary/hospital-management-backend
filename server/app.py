from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Doctor, Department

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

if __name__ == "__main__":
    app.run(port=5555, debug=True)