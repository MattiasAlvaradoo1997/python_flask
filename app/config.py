import os

class Config(object):
    #configuraciones de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #obtenemos la url de la base de datos desde el .env
    SQLALCHEMY_TRACK_MODIFICATIONS = False #deshabilitamos las modificaciones de la base de datos