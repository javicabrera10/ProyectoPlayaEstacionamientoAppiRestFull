from app.extensions import db

class Espacio(db.Model):

    __tablename__ = "espacios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    numero = db.Column(
        db.String(10),
        nullable=False
    )

    ocupado = db.Column(
        db.Boolean,
        default=False
    )