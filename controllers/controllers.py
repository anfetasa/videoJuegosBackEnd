from flask.views import MethodView
import json
from flask import jsonify, request
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
from flask_mysqldb import MySQL
from models.register import Register 
from models.games import Games
from models.details import Details
from validators.validator import  CreateRegisterSchema,CreateLoginSchema



class LoginUserControllers(MethodView):

    def post(self):
        login = Register()
        content = request.get_json()

        create_login_schema = CreateLoginSchema()
        errors = create_login_schema.validate(content)
        if errors:
            return errors, 400

        login.correo = content.get("correo") 
        contraseña = bytes(str(content.get("contraseña")), encoding= 'utf-8')
        answer = login.get_user()

        if answer != "":
            password_db = bytes(answer[0][3], 'utf-8')
            nombre = answer[0][1]
            if bcrypt.checkpw(contraseña, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1000), 'correo': answer[0][2], 'nombre': answer[0][1]}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt), "nombre": answer[0][1], "tipousuario": answer[0][4]}), 200     
            return jsonify({"Status": "Login incorrecto 22"}), 400
        return jsonify({"Status": "Login incorrecto 11"}), 400
    
   



    

class RegisterUserControllers(MethodView):
    def post(self):
        register = Register()
        content = request.get_json()

        create_register_schema = CreateRegisterSchema()
        errors = create_register_schema.validate(content)

        if errors:
            return errors, 400

        nombre = content.get("nombre")
        correo = content.get("correo")
        contraseña = content.get("contraseña")

        salt = bcrypt.gensalt()
        register.contraseña = bcrypt.hashpw(bytes(str(contraseña), encoding= 'utf-8'), salt)
        register.nombre = nombre
        register.correo = correo
        message = register.add_user()
        
        messagegmail = register.gmail()


        return jsonify({"Status": "Registro ok",
                        "password_plano": contraseña}), 200
    

class HomeControllers(MethodView):

    def get(self):
        ga = Games()
        answer = ga.get_games()
        return jsonify(answer)
    

class ToPostControllers(MethodView):
    def post(self):
        games = Games()
        content = request.get_json()

        nombre = content.get("nombre")
        descripcion = content.get("descripcion")
        precio = content.get("precio")
        categoria = content.get("categoria")
        img = content.get("img")
        
        games.nombre = nombre
        games.descripcion = descripcion
        games.precio = precio
        games.categoria = categoria
        games.img = img
        message = games.add_games()
        
        return jsonify({"Status": "To post Ok",
                        }), 200



class StockControllers(MethodView):
 
    def get(self,id):
        details = Details()
        details.id = int(id)
        answer= details.GetDetails()
        return jsonify(answer), 200

class CarritoControllers(MethodView):

    def post(self):
        datos_token = ""
        correo = ""
        tokenR = request.headers.get('Authorization').split(" ")
        token = tokenR[1]
       
        datos_token = jwt.decode(token, KEY_TOKEN_AUTH , algorithms=['HS256'])
        correo = datos_token.get("correo")

        json_req = request.get_json(force=True)
        idJuego = json_req["idJuego"]

        carrito = Games()
        
        carrito.idUsuario = correo
        carrito.idJuego = idJuego

        message = carrito.add_carrito()

        return jsonify({"Status": "carrito Ok",
                        }), 200


class CarritoStockControllers(MethodView):

    def post(self, id, token):
        
        datos_token = ""
        correo = ""
        tokenR = request.headers.get('Authorization').split(" ")
        token = tokenR[1]
       
        datos_token = jwt.decode(token, KEY_TOKEN_AUTH , algorithms=['HS256'])
        correo = datos_token.get("correo")

        carrito = Games()
        carrito.correo = correo

        answer = carrito.get_games_carrito()
        return jsonify(answer)

    def delete(self, id, token):

        datos_token = ""
        correo = ""
       
        datos_token = jwt.decode(token, KEY_TOKEN_AUTH , algorithms=['HS256'])
        correo = datos_token.get("correo")
        
        carrito = Games()

        carrito.correo = correo
        carrito.idJuego = id

        message = carrito.delete_carrito()

        answer = carrito.get_games_carrito()
        return jsonify(answer)


class BuyStockControllers(MethodView):
    def post(self):

        tokenR = request.headers.get('Authorization').split(" ")
        token = tokenR[1]
       
        datos_token = jwt.decode(token, KEY_TOKEN_AUTH , algorithms=['HS256'])
        correo = datos_token.get("correo")

        json_req = request.get_json(force=True)
        juegos = json_req["juegos"]

        carrito = Games()

        carrito.juegos = juegos
        carrito.correo = correo

        answer = carrito.registro_compras()
        andwer = carrito.delete_All_carrito()
        
        
        return jsonify({"Status": "Ok",
                        }), 200

class RegistroCompraControllers(MethodView):

    def post(self, id, token):
        
        datos_token = ""
        correo = ""
        tokenR = request.headers.get('Authorization').split(" ")
        token = tokenR[1]
       
        datos_token = jwt.decode(token, KEY_TOKEN_AUTH , algorithms=['HS256'])
        correo = datos_token.get("correo")

        registro = Games()
        registro.correo = correo

        answer = registro.get_registro_compras()
        return jsonify(answer)