#importa modulo os que accede a variables de entorno y 
# maneja las rutas del sistema
import os
from dotenv import load_dotenv
 
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    #esto indica que base de datos usar 
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    #Esto desactiva un sistema interno de seguimiento de cambios.
    SQLALCHEMY_TRACK_MODIFICATIONS = False