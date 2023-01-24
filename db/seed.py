from app import db #importamos la db
from app.models import * #importamos los modelos

#Creamos una institución
institucion = Institucion(nombre='Institución1', descripcion='Descripción de la institución 1', direccion='Dirección de la institución 1', fecha_creacion='01/01/2020')
db.session.add(institucion)
db.session.commit()

#Creamos un proyecto
proyecto = Proyecto(nombre='Proyecto1', descripcion='Descripción del proyecto 1', fecha_inicio='01/02/2020', fecha_termino='01/03/2020', usuario_id=1)
db.session.add(proyecto)
db.session.commit()

#Creamos un usuario
usuario = Usuario(nombre='Usuario1', apellidos='Apellidos del usuario 1', rut='12345678-9', fecha_nacimiento='01/01/2000', cargo='Cargo del usuario 1', edad=20)
db.session.add(usuario)
db.session.commit()