from flask import Blueprint,render_template


from app.models.egreso import Egreso
from app.models.espacio import Espacio

egreso_bp = Blueprint("egreso_bp",__name__)


# GET EGRESOS
@egreso_bp.route("/egresos", methods=["GET"])
def obtener_egresos():

    espacios = Espacio.query.filter_by(ocupado = False).all()

    return render_template("egresos.html",espacios=espacios)