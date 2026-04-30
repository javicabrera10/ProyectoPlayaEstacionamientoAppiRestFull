#Acá estás importando una función llamada create_app desde el paquete app.
from app import create_app


# aca ejecutas las funcion Se crea el objeto principal de Flask (app)
app = create_app()
# lo que hay dentro de la condicion se ejecuta si corrés este archivo directamente
if __name__ == "__main__":
    app.run(debug=True) #corre la aplicacion y activa el modo desarrollo
    