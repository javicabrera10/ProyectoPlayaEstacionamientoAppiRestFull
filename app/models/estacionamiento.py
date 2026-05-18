from app.extensions import db
from app.models.base_model import BaseModel # Heredamos de tu molde maestro
from datetime import datetime

# 1. Tabla para registrar los vehículos
class Vehiculo(BaseModel):
    __tablename__ = 'vehiculos'
    
    patente = db.Column(db.String(20), unique=True, nullable=False)
    marca = db.Column(db.String(50), nullable=True)
    modelo = db.Column(db.String(50), nullable=True)

# 2. Tabla para registrar los ingresos de los autos
class Ingreso(BaseModel):
    __tablename__ = 'ingresos'
    
    fecha_entrada = db.Column(db.DateTime, default=datetime.now)
    cochera_asignada = db.Column(db.Integer, nullable=False) # Número de lugar
    estado = db.Column(db.String(20), default="Activo") # Para saber si todavía está adentro
    
    # Conectamos con el vehículo mediante su ID
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)

# 3. Tabla para registrar los egresos (salidas y cobros)
class Egreso(BaseModel):
    __tablename__ = 'egresos'
    
    fecha_salida = db.Column(db.DateTime, default=datetime.now)
    total_pago = db.Column(db.Float, nullable=False)
    
    # Conectamos con el ingreso original para saber qué auto salió y cuánto tiempo estuvo
    ingreso_id = db.Column(db.Integer, db.ForeignKey('ingresos.id'), nullable=False)