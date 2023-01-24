from flask import request, jsonify
from app import app, db
from app.models import *

#CRUD Instituciones

#Crear una institución
@app.route('/instituciones', methods=['POST'])
def crear_institucion():
    data = request.get_json()
    nombre = data['nombre']
    descripcion = data['descripcion']
    direccion = data['direccion']
    fecha_creacion = data['fecha_creacion']

    institucion = Institucion(nombre=nombre, descripcion=descripcion, direccion=direccion, fecha_creacion=fecha_creacion)

    db.session.add(institucion)
    db.session.commit()

    return jsonify({'msg': 'Institución creada'})

#Leer una institución
@app.route('/instituciones/<int:id>', methods=['GET'])
def leer_institucion(id):
    institucion = Institucion.query.get(id)

    if not institucion:
        return jsonify({'msg': 'No existe institución'})

    return jsonify({'institucion': {
        'id': institucion.id,
        'nombre': institucion.nombre,
        'descripcion': institucion.descripcion,
        'direccion': institucion.direccion,
        'fecha_creacion': institucion.fecha_creacion
    }})

#Actualizar una institución
@app.route('/instituciones/<int:id>', methods=['PUT'])
def actualizar_institucion(id):
    data = request.get_json()
    nombre = data['nombre']
    descripcion = data['descripcion']
    direccion = data['direccion']
    fecha_creacion = data['fecha_creacion']

    institucion = Institucion.query.get(id)

    if not institucion:
        return jsonify({'msg': 'No existe institución'})

    institucion.nombre = nombre
    institucion.descripcion = descripcion
    institucion.direccion = direccion
    institucion.fecha_creacion = fecha_creacion

    db.session.commit()

    return jsonify({'msg': 'Institución actualizada'})

#Borrar una institución
@app.route('/instituciones/<int:id>', methods=['DELETE'])
def borrar_institucion(id):
    institucion = Institucion.query.get(id)

    if not institucion:
        return jsonify({'msg': 'No existe institución'})

    db.session.delete(institucion)
    db.session.commit()

    return jsonify({'msg': 'Institución borrada'})

#Listar todas las instituciones
@app.route('/instituciones', methods=['GET'])
def listar_instituciones():
    instituciones = Institucion.query.all()
    lista = []

    for institucion in instituciones:
        lista.append({
        'id': institucion.id,
        'nombre': institucion.nombre,
        'descripcion': institucion.descripcion,
        'direccion': institucion.direccion,
        'fecha_creacion': institucion.fecha_creacion
        })

    return jsonify({'instituciones': lista})

#Listar institución (Filtrada por id) con sus respectivos proyectos y responsable del proyecto
@app.route('/instituciones/<int:id>/proyectos', methods=['GET'])
def listar_institucion_proyectos(id):
    institucion = Institucion.query.get(id)

    if not institucion:
        return jsonify({'msg': 'No existe institución'})

    proyectos = institucion.proyectos

    lista = []

    for proyecto in proyectos:
        lista.append({
        'id': proyecto.id,
        'nombre': proyecto.nombre,
        'descripcion': proyecto.descripcion,
        'fecha_inicio': proyecto.fecha_inicio,
        'fecha_termino': proyecto.fecha_termino,
        'usuario': proyecto.usuario.nombre
        })

    return jsonify({'proyectos': lista})

#Listar usuario (Filtrada por rut) con sus respectivos proyectos
@app.route('/usuarios/<string:rut>/proyectos', methods=['GET'])
def listar_usuario_proyectos(rut):
    usuario = Usuario.query.filter_by(rut=rut).first()

    if not usuario:
        return jsonify({'msg': 'No existe usuario'})

    proyectos = usuario.proyecto

    lista = []

    for proyecto in proyectos:
        lista.append({
        'id': proyecto.id,
        'nombre': proyecto.nombre,
        'descripcion': proyecto.descripcion,
        'fecha_inicio': proyecto.fecha_inicio,
        'fecha_termino': proyecto.fecha_termino
        })

    return jsonify({'proyectos': lista})

#Listar instituciones donde a cada institución se agregue a la dirección la ubicación de google maps ejemplo: “https://www.google.com/maps/search/+ direccion ” y la abreviación del nombre (solo los primeros tres caracteres).
@app.route('/instituciones/direccion-abrev', methods=['GET'])
def listar_instituciones_direccion_abrev():
    instituciones = Institucion.query.all()

    lista = []

    for institucion in instituciones:
        lista.append({
        'id': institucion.id,
        'nombre': institucion.nombre,
        'descripcion': institucion.descripcion,
        'direccion': institucion.direccion,
        'fecha_creacion': institucion.fecha_creacion,
        'direccion_google': 'https://www.google.com/maps/search/' + institucion.direccion,
        'abrev': institucion.nombre[:3]
        })

    return jsonify({'instituciones': lista})

#Listar los proyectos que la respuesta sea el nombre del proyecto y los días que faltan para su término.
@app.route('/proyectos/faltan-dias', methods=['GET'])
def listar_proyectos_falta_dias():
    proyectos = Proyecto.query.all()

    lista = []

    for proyecto in proyectos:
        lista.append({
        'nombre': proyecto.nombre,
        'faltan_dias': proyecto.fecha_termino - proyecto.fecha_inicio
        })

    return jsonify({'proyectos': lista})
