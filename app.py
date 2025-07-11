from flask import Flask, render_template, request, redirect, url_for
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db, Estudiante

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        matricula = request.form['matricula']
        carrera = request.form['carrera']
        nuevo = Estudiante(nombre=nombre, matricula=matricula, carrera=carrera)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    estudiante = Estudiante.query.get_or_404(id)
    if request.method == 'POST':
        estudiante.nombre = request.form['nombre']
        estudiante.matricula = request.form['matricula']
        estudiante.carrera = request.form['carrera']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', estudiante=estudiante)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    estudiante = Estudiante.query.get_or_404(id)
    db.session.delete(estudiante)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
