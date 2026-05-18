#importa modulo os que accede a variables de entorno y 
# maneja las rutas del sistema
import os

class Config:
    SECRET_KEY = "super_secret_key"#Eso evita hardcodear claves sensibles.
    #esto indica que base de datos usar 
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/db_flask"
    #Esto desactiva un sistema interno de seguimiento de cambios.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    