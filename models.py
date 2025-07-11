from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    matricula = db.Column(db.String(50), nullable=False, unique=True)
    carrera = db.Column(db.String(100), nullable=False)
