#Blueprint → sirve para organizar rutas en módulos (clave en MVC)
#request → te permite leer datos que envía el cliente (JSON, form, etc.)
#jsonify → convierte datos Python a JSON (respuesta de API)


from flask import Blueprint, request, jsonify
from app.controllers import base_controller

#Acá creás un Blueprint.
#"base_bp" → nombre del blueprint
#__name__ → ayuda a Flask a ubicar archivos
base_bp = Blueprint("base_bp", __name__)

@base_bp.route("/", methods=["GET"])#Esto es un decorador que define una ruta.
#Cuando alguien hace un GET a /, se ejecuta la función de abajo.
#Blueprint → organiza rutas
#@route → define endpoint
#home() → lógica de respuesta
#jsonify → devuelve JSON
def home():

    return jsonify({"mensaje": "API funcionando"})