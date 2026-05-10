from flask import Blueprint
from flask import request
from flask import render_template
from flask import redirect

from app.extensions import db
from app.models.vehiculo import Vehiculo

# Blueprint
vehiculo_bp = Blueprint("vehiculo_bp",__name__)

# GET
@vehiculo_bp.route("/vehiculos", methods=["GET"])
def obtener_vehiculos():

    vehiculos = Vehiculo.query.all()

    return render_template(
        "crear_vehiculo.html",
        vehiculos=vehiculos
    )

# POST
@vehiculo_bp.route("/vehiculos", methods=["POST"])
def crear_vehiculo():

    data = request.form

    nuevo_vehiculo = Vehiculo(
        modelo=data["modelo"],
        patente=data["patente"],
        color=data["color"],
        tipo=data["tipo"]
    )

    db.session.add(nuevo_vehiculo)
    db.session.commit()

    return redirect("/vehiculos")