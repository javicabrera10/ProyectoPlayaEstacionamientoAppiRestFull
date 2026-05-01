#Acá estás importando una función llamada create_app desde el paquete app.
from app import create_app

from app.extensions import db 

# aca ejecutas las funcion Se crea el objeto principal de Flask (app)
app = create_app()

#Activa el “contexto de la aplicación” de Flask de forma temporal.
with app.app_context():
   
    db.create_all() #crea las tablas automaticas a partir de tu modelo



# lo que hay dentro de la condicion se ejecuta si corrés este archivo directamente
if __name__ == "__main__":
    app.run(debug=True) #corre la aplicacion y activa el modo desarrollo
    