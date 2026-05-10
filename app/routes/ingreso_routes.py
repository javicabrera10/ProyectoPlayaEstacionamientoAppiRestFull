from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from app.models.ingreso import Ingreso
from app.extensions import db

ingreso_bp = Blueprint(
    "ingreso_bp",__name__)

# MOSTRAR HTML
@ingreso_bp.route("/ingresos", methods=["GET"])
def obtener_ingresos():

    ingresos = Ingreso.query.all()

    return render_template("ingresos.html",ingresos=ingresos)


# CREAR INGRESO
@ingreso_bp.route("/ingresos", methods=["POST"])
def crear_ingreso():

    patente = request.form["patente"]

    nuevo_ingreso = Ingreso(
        patente=patente
    )

    db.session.add(nuevo_ingreso)
    db.session.commit()

    return redirect("/ingresos")