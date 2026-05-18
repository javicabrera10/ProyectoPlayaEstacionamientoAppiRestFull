#Define una función que recibe un modelo (por ejemplo Usuario, Turno, etc.)
def get_all(model):
    return model.query.all()#model.query → accede al sistema de consultas de SQLAlchemy
#.all() → trae todos los registros
def get_by_id(model, id):#Busca un registro por su clave primaria (id)(trae uno)
    return model.query.get(id)#

def create(model, data):#Esto crea una instancia del modelo dinámicamente.
    obj = model(**data)
    obj.save()#se agrega el objeto a la sesion
    return obj

def delete(model, id):
    obj = model.query.get(id)#Busca el objeto por id
    if obj:#verifica si existe
        obj.delete()#elimina y hace commit
        return True#indica que se elimino correctamente
    return False