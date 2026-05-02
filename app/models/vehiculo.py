from app.extensions import db

class Vehiculo(db.Model):
    __tablename__ = "vehiculos"

    # acá va la tabla vehiculos
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    modelo = db.Column(db.String(50),nullable=False) 
    patente = db.Column(db.String(10), unique=True,nullable=False) #nullable = obligatorio
    color = db.Column(db.String(20),nullable=False) 
    tipo = db.Column(db.String(10),nullable=False)