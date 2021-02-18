
from flask.views import MethodView
from flask import jsonify, request
from model import users
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime



class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):

        content = request.get_json()
        correo = content.get("correo")
        contraseña = bytes(str(content.get("contraseña")), encoding= 'utf-8')
        print(correo)
        if users.get(correo):
            password_db = users[correo]["contraseña"]
            if bcrypt.checkpw(contraseña, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300), 'correo': correo}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": encoded_jwt}), 200
            return jsonify({"Status": "Login incorrecto 22"}), 400
        return jsonify({"Status": "Login incorrecto 11"}), 400
    

class RegisterUserControllers(MethodView):

    def post(self):

        content = request.get_json()
        nombre = content.get("nombre")
        correo = content.get("correo")
        contraseña = content.get("contraseña")

        salt = bcrypt.gensalt()
        hash_password = bcrypt.hashpw(bytes(str(contraseña), encoding= 'utf-8'), salt)

        users[correo] = {"contraseña": hash_password, "nombre": nombre}
        return jsonify({"Status": "Registro ok",
                        "password_encriptado": str(hash_password),
                        "password_plano": contraseña}), 200
    


class HomeControllers(MethodView):

    def post(self):
        
        return jsonify({"hola"}), 200


class CarritoControllers(MethodView):

    def post(self):
        
        return jsonify({"hola"}), 200
    

class InicioVendedorControllers(MethodView):
    """
        Example vendedor
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        correo = content.get("correo")
        contraseña = content.get("contraseña")

        return jsonify({"register ok": True, "correo": correo, "contraseña": contraseña}), 200


class StockControllers(MethodView):
 
    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email"), "stock": {"nombre": "xbox", "precio": 1200000}}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
            return jsonify({"Status": "No ha enviado un token"}), 403
     
