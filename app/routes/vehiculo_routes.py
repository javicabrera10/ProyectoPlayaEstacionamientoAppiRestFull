#para post se importa lo de abajo
from flask import request #Importás request
#Sirve para acceder a los datos que manda el cliente (Postman, frontend, etc.)
from app.extensions import db  #Importás la conexión a la base de datos

#para get se importa lo de abajo
from flask import Blueprint, jsonify

#importar la clase vehiculo
from app.models.vehiculo import Vehiculo

#crear el blueprint
vehiculo_bp = Blueprint("vehiculo_bp", __name__)

@vehiculo_bp.route("/vehiculos", methods=["GET"])
def obtener_vehiculos():
    vehiculos = Vehiculo.query.all()

    resultado = []
    #resultado va traer los atributos de cada vehiculo que hay en vehiculos

    for v in vehiculos:
        resultado.append({
            "id":v.id,
            "modelo":v.modelo,
            "patente":v.patente,
            "color": v.color,
            "tipo": v.tipo
        })

    return jsonify(resultado)

#post
#Definís la ruta
#POST = crear datos nuevos
#
@vehiculo_bp.route("/vehiculos", methods=["POST"])
def crear_vehiculo():#Función que se ejecuta cuando alguien hace POST
    data = request.json #Acá recibís los datos enviados en formato JSON

    nuevo_vehiculo = Vehiculo(
        modelo=data["modelo"],#Tomás el dato del JSON y lo asignás al atributo
        patente=data["patente"],
        color=data["color"],
        tipo=data["tipo"]
    )
    #Preparás el objeto para guardarlo en la BD
    db.session.add(nuevo_vehiculo)
    #se guarda definitivamente en MySQL
    db.session.commit()
    #retorna el json con el mensaje
    return jsonify({"mensaje": "Vehiculo creado correctamente"}), 201