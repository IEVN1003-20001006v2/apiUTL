from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import config
 
app = Flask(__name__)
CORS(app, resources={r"/alumnos/*": {"origins": "http://localhost:4200"}})
conexion = MySQL(app)
 
@app.route("/alumnos", methods=["GET"])
def lister_alumnos():
    try:
        cursor = conexion.connection.cursor()  # Cambié connection a conexion
        sql = "SELECT * FROM alumnos ORDER BY nombre ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
       
        alumnos = []
        for fila in datos:
            alumno = {
                "matricula": fila[0],  # Cambié la estructura de los datos
                "nombre": fila[1],
                "apaterno": fila[2],
                "amaterno": fila[3],
                "correo": fila[4]  # Corregí el nombre de la clave
            }
            alumnos.append(alumno)
       
        cursor.close()  # Cierra el cursor después de usarlo
        return jsonify({'alumnos': alumnos, 'mensaje': 'Alumnos listados', "exito": True})
   
    except Exception as ex:
        return jsonify({"mensaje": "Error al conectar con la DB: {}".format(ex), 'exito': False})
 
def pagina_no_encontrada(error):
    return jsonify({"mensaje": "Error 404: {}".format(error), 'exito': False})
 
if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)  # Cambié 400 a 404
    app.run()