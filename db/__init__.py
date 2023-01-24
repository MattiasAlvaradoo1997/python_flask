from app import db #importamos la db

#importamos los modelos
from .seed import *
#inicializamos la base de datos
db = SQLAlchemy(app, scopefunc=_app_ctx_stack.__ident_func__)
