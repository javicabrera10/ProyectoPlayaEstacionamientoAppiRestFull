from app.extensions import db
from datetime import datetime

class Egreso(db.Model):

    __tablename__ = "egresos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    patente = db.Column(
        db.String(10),
        nullable=False
    )

    fecha_egreso = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {
            "id": self.id,
            "patente": self.patente,
            "fecha_egreso": self.fecha_egreso
        }