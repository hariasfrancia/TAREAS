# nos sirve para que cuando nos traiga la base datos nos sdevuelva como un Json
from flask_marshmallow import Marshmallow

#Lo instanciamos con una variable (ma) llamando a Marshmallow
hd = Marshmallow()

#declaranmos una clase que va heredar de schema
class HelpDeskSchema(hd.Schema):
    class Meta:
        fields = ('id','titulo_caso','descripcion_caso','fecha_creacion')

#creamos variable donde almacenamos e instanciamos la clase
helpdesk_schema = HelpDeskSchema()
#otro esquema para traer mas esqueas
helpdesks_schema = HelpDeskSchema(many=True)
