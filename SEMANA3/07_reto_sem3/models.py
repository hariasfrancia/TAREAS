#Aca crearemos nustras tablas
from flask_sqlalchemy import SQLAlchemy
import datetime

#guardamos nuestra base de datos como "db", que es una istancia de sqlalchemy
db = SQLAlchemy()

#En nuestra base datos crearemos nuestras tablas, utilizamos POO, con nuestro ORM definimos nuestras tablas creando nuestra clase HelpDEsk que herada de "db.Model" quees una propiedad para crear modelos
class HelpDesk(db.Model):
    __tablename__ = 'atencion'
    #definimos las columnas
    id = db.Column(db.Integer, primary_key=True)
    titulo_caso = db.Column(db.String(80), unique=True)
    descripcion_caso = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, default = datetime.datetime.now)
    #Instanciamos y usamos un constructor llamado (__init__) propia de PYTHON
    def __init__(self, titulo_caso, descripcion_caso):
        self.titulo_caso = titulo_caso
        self.descripcion_caso = descripcion_caso



