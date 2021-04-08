ENTORNO VIRTUAL USANDO LA LIBRERIA:  virtualenv
==================================
1.-PRIMER PASO
   ===========
    -Instalar la libreria virtualenv:
     #pip install virtualenv
2.-SEGUNDO PASO
   ============     
    -Crar elentorno virtual:
     #virtualenv venv
3.-TERCER PASO
   ===========
    -Activar el entorno virtual
    #venv\Scripts\activate.bat
4.-CUARTO PASO
   ===========
    -Instalando flask
     #pip install flask
5.-QUINTO PASO
   ===========
    -Instalando flask-cors
     #pip install flask-cors
6.-SEXTO PASO
   ===========
    -Instalando flask-sqlalchemy
     #pip install flask-cors flask-sqlalchemy
7.-SEPTIMO PASO
   ===========
    -Instalando flask-marshmallow
     #pip install flask-cors flask-sqlalchemy flask-marshmallow
8.-OCTAVO PASO
   ===========
    -Instalando marshmallow-sqlalchemy
     #pip install flask-cors flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
8.-OCTAVO PASO(Ultimo paso a ejecutar en una sola linea)
   ============
    -Instalando mysqlclient
     #pip install flask-cors flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy mysqlclient
9.-NOVENO PASO
   ===========
   -Creamos app.py y probamos quelevante el servicio
   -Jalamos las librerias (from flask import Flask - from flask_cors import CORS)
   -#instanciando Flask
   -#configuramos la ruta raiz
   -#Levantando el servidor
   -ejecutamos el comando python app.py para levantar el servicio
9.-NOVENO PASO
   ===========
   -Creamos nuestro archivo models.py, aqui se va a modelar nustra base de datos
10.-DECIMO PASO
   ===========
   -Creamos nuestro archivo schemas.py, es un proceso de limpieza con la libreria marshmallow
11.-ONCEAVO PASO
   ===========
   -creamos el archivo models, con:
    #Aca crearemos nustras tablas
    #guardamos nuestra base de datos como "db", que es una istancia de sqlalchemy
    #En nuestra base datos crearemos nuestras tablas, utilizamos POO, con nuestro ORM definimos nuestras tablas creando nuestra clase HelpDEsk que herada de "db.Model" quees una propiedad para crear modelos
    #definimos las columnas
    #Instanciamos y usamos un constructor llamado (__init__), propia de python
12.-DOCEAVO PASO
   ===============
   -Nos vamos al archivo APP.py para realizar la conexion
   -#Traernos desde models lo creado
      from models import db
      from models import HelpDesk
   -#Configurando la conexion a la base datos
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/repasoflask'
      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   -Creamos nuestra base de datos en el Worbench con el comando: create database Mesa_Ayuda;

13.-TRECEAVO PASO
   ===============
   -#SQLAlchemy tiene la propiedad de relacionar la base datos con la aplicacion y con esto   se dirige a la config de la aplicacion
    db.init_app(app)
   -#Busca todos los modelos que se especifico dentro de SQLAlchemy y verifica si lo a creado
    db.create_all()
   -#definimos (with) para sincronizar nuestra base de datos
    with app.app_context(app):
      db.create_all()

14.-CATORCEAVO PASO
   ================
   -CORRER el archivo app.py el la consola con: python app.py

15.-QUINCEAVO PASO
   ================
   -Ahora trabajamos con el archivo schemas.py
   -importamos from flask_marshmallow import Marshmallow
   -#Lo instanciamos con una variable (ma) llamando a Marshmallow
    hd = Marshmallow()
   -#declaranmos una clase que va heredar de schema
   -#creamos variable donde almacenamos e instanciamos la clase
   -#otro esquema para traer mas esqueas

16.-DIECISEISCEAVO PASO
   ================
   -#importando los esquemas
   -from schemas import hd
   -from schemas import HelpDesk_schema
   -from schemas import HelpDesks_schema
   - dentro de (if __name__ == '__main__':) pasamos la linea "hd.init_app(app)"
   