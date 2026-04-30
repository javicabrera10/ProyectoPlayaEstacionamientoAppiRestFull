#Importás db, que es la instancia de SQLAlchemy que definiste antes.
from app.extensions import db

#Creás una clase llamada BaseModel que hereda de db.Model.
class BaseModel(db.Model):
    __abstract__ = True  # No crea tabla

    #Definís un campo común para todos los modelos.
    id = db.Column(db.Integer, primary_key=True)

    def save(self):#Define un método para guardar el objeto.
        db.session.add(self)#Agrega el objeto actual (self) a la sesión.
        db.session.commit()#Ejecuta el guardado en la base de datos.

    def delete(self):
        db.session.delete(self)#Marca el objeto para eliminación.
        db.session.commit()#Ejecuta el DELETE en la base de datos.