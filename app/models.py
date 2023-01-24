from app import db #importamos la db

#Creamos la clase institucion
class Institucion(db.Model):
    __tablename__ = 'instituciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)
    direccion = db.Column(db.String)
    fecha_creacion = db.Column(db.String)

#Creamos la clase proyecto
class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)
    fecha_inicio = db.Column(db.String)
    fecha_termino = db.Column(db.String)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

#Creamos la clase usuario
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    apellidos = db.Column(db.String)
    rut = db.Column(db.String)
    fecha_nacimiento = db.Column(db.String)
    cargo = db.Column(db.String)
    edad = db.Column(db.Integer)
    proyecto = db.relationship('Proyecto', backref='usuario', lazy=True)
