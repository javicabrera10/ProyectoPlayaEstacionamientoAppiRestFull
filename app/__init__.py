from flask import Flask
from app.routes.base_routes import base_bp
from app.config import Config
from app.extensions import db
from app.models.estacionamiento import Vehiculo, Ingreso, Egreso
def create_app():
    #flask usa name para ubicar rutas de archivos
    app = Flask(__name__)
    #“Tomá todos los atributos de la clase Config y usalos como configuración”
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    # Crear tablas en la base de datos si no existen
    with app.app_context():
        db.create_all()

    # Registrar blueprints
    app.register_blueprint(base_bp)

    return app