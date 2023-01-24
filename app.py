from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

#inicializamos la app
app = Flask(__name__)

#configuramos la app
app.config.from_object(Config)

#inicializamos la base de datos
db = SQLAlchemy(app)

#importamos los modelos
from app.models import *

#importamos las rutas
from app import routes
app.app_context().push()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False