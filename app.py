from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email
        }

def init_db():
    with app.app_context():
        db.create_all()
        db.session.query(Student).delete()
        sample_students = [
            Student(name='Alice', age=20, email='alice@example.com'),
            Student(name='Bob', age=22, email='bob@example.com'),
            Student(name='Charlie', age=23, email='charlie@example.com'),
            Student(name='David', age=21, email='david@example.com'),
            Student(name='Eve', age=24, email='eve@example.com')
        ]
        db.session.bulk_save_objects(sample_students)
        db.session.commit()

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(code=200, message='success', data={})

@app.route('/students', methods=['GET'])
def get_students():
    with app.app_context():
        students = Student.query.all()
        return jsonify(code=200, message='success', data=[student.to_dict() for student in students])

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if not data or 'name' not in data or 'age' not in data or 'email' not in data:
        return jsonify(code=400, message='Invalid input', data={})
    
    with app.app_context():
        new_student = Student(name=data['name'], age=data['age'], email=data['email'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify(code=200, message='success', data=new_student.to_dict())

@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
    if not id.isdigit():
        return jsonify(code=400, message='Invalid ID', data={})
    
    data = request.json
    if not data or 'name' not in data or 'age' not in data or 'email' not in data:
        return jsonify(code=400, message='Invalid input', data={})

    with app.app_context():
        student = Student.query.get_or_404(int(id))
        student.name = data['name']
        student.age = data['age']
        student.email = data['email']
        db.session.commit()
        return jsonify(code=200, message='success', data=student.to_dict())

@app.route('/students/<id>', methods=['DELETE'])
def delete_student(id):
    if not id.isdigit():
        return jsonify(code=400, message='Invalid ID', data={})

    with app.app_context():
        student = Student.query.get_or_404(int(id))
        db.session.delete(student)
        db.session.commit()
        return jsonify(code=200, message='success', data={})

@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    if not id.isdigit():
        return jsonify(code=400, message='Invalid ID', data={})

    with app.app_context():
        student = Student.query.get_or_404(int(id))
        return jsonify(code=200, message='success', data=student.to_dict())

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8020, debug=False)
