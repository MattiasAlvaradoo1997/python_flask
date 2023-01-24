from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

#instanciamos la app
app = Flask(__name__)

#importamos la configuracion de la aplicacion
app.config.from_object(Config)

#instanciamos la db
db = SQLAlchemy(app)

#configuramos la migracion
migrate = Migrate(app, db)

#importamos los modelos
from .models import *

#importamos las rutas
from .routes import *
#inicializamos la base de datos
db = SQLAlchemy(app, scopefunc=_app_ctx_stack.top)
app.app_context().push()