from flask import Flask, request, render_template
from conexion import BaseDeDatos

# se instancia la base de datos para poder usarla en el proyecto
db = BaseDeDatos()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estudiantes')
def estudiantes():
    estudiantes = db.leer_tabla('estudiantes')
    return render_template('estudiantes.html', estudiantes=estudiantes)

@app.route('/cursos')
def cursos():
    cursos = db.leer_tabla('cursos')
    return render_template('cursos.html', cursos=cursos)


if __name__ == '__main__':
    app.run(debug=True)
