from flask import Flask, request, jsonify
from flask_cors import CORS

#Traernos desde models lo creado y SQLAlchemy
from models import db
from models import HelpDesk

#importando los esquemas
from schemas import hd
from schemas import helpdesk_schema
from schemas import helpdesks_schema

#instanciando Flask
app = Flask(__name__)
#configuramos CORS
CORS(app)

#Configurando la conexion a la base datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/mesa_ayuda'
#Para queno lanse el wuarning de error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#configuramos la ruta raiz
@app.route('/')
def inicio():
    return 'Probamos que levanto el servicio de Flask'
#////////////////////////////////////////////////////////
#Ruta para obtener y agregar tareas
@app.route('/api/ayudas', methods=['GET','POST'])
def manage_helpdesks():
    if request.method == 'POST':
        titulo_caso = request.json['titulo_caso']
        descripcion_caso = request.json['descripcion_caso']
        nueva_ayuda = HelpDesk(titulo_caso, descripcion_caso) #hace referencia a una instancia
        db.session.add(nueva_ayuda)
        db.session.commit()
        return helpdesk_schema.jsonify(nueva_ayuda)
    elif request.method == 'GET':
        todas_las_ayudas = HelpDesk.query.all()
        result = helpdesks_schema.dump(todas_las_ayudas)
        return jsonify(result)
#///////////////////////////////////////////////////////
@app.route('/api/ayudas/<id>',methods=['GET','DELETE','PUT'])
def manage_helpdesk(id):
    if request.method == 'GET':
        ayuda = HelpDesk.query.get(id)
        return helpdesk_schema.jsonify(ayuda)
    elif request.method == 'PUT':
        ayuda = HelpDesk.query.get(id)
        titulo_caso = request.json['titulo_caso']
        descripcion_caso = request.json['descripcion_caso']
        ayuda.titulo_caso = titulo_caso
        ayuda.descripcion_caso = descripcion_caso
        db.session.commit()
        return helpdesk_schema.jsonify(ayuda)
    elif request.method == 'DELETE':
        ayuda = HelpDesk.query.get(id)
        db.session.delete(ayuda)
        db.session.commit()
        return helpdesk_schema.jsonify(ayuda)
#///////////////////////////////////////////////////////

#Levantando el servidor
if __name__ == '__main__':
    #SQLAlchemy tiene la propiedad de relacionar la base datos con la aplicacion y con esto se dirige a la config de la aplicacion
    db.init_app(app)
    hd.init_app(app)
    #definimos (with) para sincronizar nuestra base de datos
    with app.app_context():
        #Busca todos los modelos que se especifico dentro de SQLAlchemy y verifica si lo a creado
        db.create_all() 

app.run(port=7000, debug=True)