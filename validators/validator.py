from marshmallow import Schema, fields
from marshmallow import validate, ValidationError

class CreateRegisterSchema(Schema):

    nombre = fields.Str(required=True, validate=validate.Length(min=4, max=60))
    
    correo = fields.Str(required=True, validate=validate.Email())

    contraseña = fields.Str(required=True, validate=validate.Length(min=6, max=40))



class CreateLoginSchema(Schema):

    correo = fields.Str(required=True, validate=validate.Email())

    contraseña = fields.Str(required=True, validate=validate.Length(min=6, max=40))