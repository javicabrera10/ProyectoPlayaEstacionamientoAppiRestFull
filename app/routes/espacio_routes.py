from flask import Blueprint, render_template
from app.models.espacio import Espacio

espacio_bp = Blueprint ("espacio_bp",__name__)

@espacio_bp.route("/espacios",methods=["GET"])
def obtener_espacios():
    #traeme solo los espacios libres
    espacios= Espacio.query.filter_by(ocupado=False).all()

    return render_template("espacios.html", espacios=espacios)