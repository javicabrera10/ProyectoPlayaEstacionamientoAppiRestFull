# Sistema de Playa de Estacionammiento

Proyecto realizado con Flask siguiendo el patrón MVC.

## Integrantes: Marcelo Britos y Javier Cabrera

## Tecnologías utilizadas

- Python
- Flask
- SQLAlchemy
- PyMysql
- HTML
- CSS
- Jinja2
- 

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/javicabrera10/ProyectoPlayaEstacionamientoAppiRestFull.git
```

### 2. Entrar al proyecto

```bash
cd "ProyectoPlayaEstacionamientoAppiRestFull"
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```
# NOTA: Usamos pymsql si no esta en requirements.txt debe instalarlo con comando:
pip install pymysql
---

## Configuración de la base de datos

Crear una base de datos en MySQL llamada:

```sql
CREATE DATABASE db_flask;
```

Configurar las variables en el archivo:

```python
config.py
```

Ejemplo:

```python
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/db_flask"
```

---

## Ejecutar el proyecto

```bash
python run.py
```

o

```bash
flask run
# Importante para que funcione debe esta encendido mysql en xampp o remoto``
#para ver pagina principal en formato api solo prueba un mensaje
colocar en el navegador http://127.0.0.1:5000/
---

## Funcionalidades

- Registrar vehiculos
#Para registrar vehiculos y ver los registrados 
colocar en navegador http://127.0.0.1:5000/vehiculos

- Ingreso de vehiculos
http://127.0.0.1:5000/ingresos
- Egreso de vehiculos
http://127.0.0.1:5000/egresos
- Calcular Espacio disponible
http://127.0.0.1:5000/espacios
- se realizaron los siguientes endpoints:
get vehiculos: para mostrar los vehiculos registrados
post vehiculos: para crear o registrar un vehiculo
get ingresos: para mostrar los ingresos a la playa
post ingresos: para crear un nuevo ingreso a la playa
get egresos: para mostrar los vehiculos que abandonana el sitio.
get espacios: para mostrar los espacios disponibles de acuerdo al limite establecido


- API REST
- Arquitectura MVC
- se implementa jinja2 y se importa render_template para poder visualizar las paginas
o formularios en html y no como API json
- se importan request para los formularios en html y redirect para luego de un post 
  recargar la pagina actualizada.
---

## Estructura del proyecto

```bash
Estacionamiento/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── extensions.py
│
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

## Autor

Javier Cabrera y Marcelo Britos