from app.extensions import db
from datetime import datetime

class Ingreso(db.Model):
    __tablename__ = "ingresos"

    id = db.Column(db.Integer, primary_key=True)

    patente = db.Column(
        db.String(10),
        nullable=False
    )

    fecha_ingreso = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "patente": self.patente,
            "fecha_ingreso": self.fecha_ingreso
        }