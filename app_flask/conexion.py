# trae variables de entorno
import os
from dotenv import load_dotenv
load_dotenv()
PASSWORD_DB = os.environ.get("PASSWORD_DB")
HOST_DB = os.environ.get("HOST_DB")


from pymysql import connect

class BaseDeDatos:
    def __init__(self) -> None:
        self.conexion = connect(host=HOST_DB, db='TallerBD',
                                user='root', password=PASSWORD_DB)
        self.cursor = self.conexion.cursor()


    def insertar_estudiante(self, estudiante):
        query = "INSERT INTO estudiantes (nombre, apellido, edad) \
        VALUES (%s, %s, %s)"

        self.cursor.execute(query, (estudiante["nombre"], estudiante["apellido"], estudiante["edad"]))
        self.conexion.commit()


    def insertar_curso(self, curso):
        query = "INSERT INTO cursos (nombre_curso, id_estudiante) \
        VALUES (%s, %s)"

        self.cursor.execute(query, (curso["nombre_curso"], curso["id_estudiante"]))
        self.conexion.commit()

    
    def leer_tabla(self, tabla):
        self.cursor.execute(f"SELECT * FROM {tabla}")
        return self.cursor.fetchall()


if __name__ == '__main__':
    # se instancia la base de datos para poder usarla en el proyecto
    db = BaseDeDatos()

    # se llena la base de datos
    datos_estudiantes = [
        {"nombre": "Alice",     "apellido": "Johnson",  "edad": 25},
        {"nombre": "Bob",       "apellido": "Smith",    "edad": 32},
        {"nombre": "Charlie",   "apellido": "Brown",    "edad": 28},
        {"nombre": "David",     "apellido": "Davis",    "edad": 40}
    ]

    datos_cursos = [
        {"nombre_curso": "Ingles",        "id_estudiante": 1},
        {"nombre_curso": "Sofware",       "id_estudiante": 1},
        {"nombre_curso": "Innovacion",    "id_estudiante": 1},
        {"nombre_curso": "Ingles",        "id_estudiante": 2},
        {"nombre_curso": "Innovacion",    "id_estudiante": 2},
        {"nombre_curso": "Software",      "id_estudiante": 3},
        {"nombre_curso": "Software",      "id_estudiante": 4},
        {"nombre_curso": "Ingles",        "id_estudiante": 4}
    ]

    for estudiante in datos_estudiantes:
        db.insertar_estudiante(estudiante)
    
    for curso in datos_cursos:
        db.insertar_curso(curso)
