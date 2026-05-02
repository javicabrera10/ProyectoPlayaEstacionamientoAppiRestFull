from flask import Flask
from app.routes.base_routes import base_bp
#importamos de routes vehiculo_routes 
from app.routes.vehiculo_routes import vehiculo_bp

from app.config import Config
from app.extensions import db

def create_app():
    #flask usa name para ubicar rutas de archivos
    app = Flask(__name__)
    #“Tomá todos los atributos de la clase Config y usalos como configuración”
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)

    # Registrar blueprints
    app.register_blueprint(base_bp)
    app.register_blueprint(vehiculo_bp)

    return app