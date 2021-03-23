from marshmallow import Schema, fields
from marshmallow import validate, ValidationError

class CreateRegisterSchema(Schema):

    nombre = fields.Str(required=True, validate=validate.Length(min=4, max=60))
    
    correo = fields.Str(required=True, validate=validate.Email())

    contraseña = fields.Str(required=True, validate=validate.Length(min=6, max=40))



class CreateLoginSchema(Schema):

    correo = fields.Str(required=True, validate=validate.Email())

    contraseña = fields.Str(required=True, validate=validate.Length(min=6, max=40))


class CreateTopostSchema(Schema):
    
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=40))

    descripcion = fields.Str(required=True, validate=validate.Length(min=10, max=200))

    precio = fields.Int(required=True, validate=validate.Range(min=1, max=10))

    categoria = fields.Str(required=True, validate=validate.Length(min=1,max=30))

    img = fields.String(required=True, validate=validate.Length(min=10, max=300))