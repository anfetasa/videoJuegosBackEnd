from flask.views import MethodView
from flask import jsonify, request
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
from flask_mysqldb import MySQL
from models.register import Register 
from models.games import Games



class LoginUserControllers(MethodView):

    def post(self):
        login = Register()
        content = request.get_json()
        login.correo = content.get("correo")
        contraseña = bytes(str(content.get("contraseña")), encoding= 'utf-8')
        answer = login.get_user()
        if answer != "":
            password_db = bytes(answer[0][3], 'utf-8')
            nombre = answer[0][1]
            if bcrypt.checkpw(contraseña, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1000), 'email': answer[0][2], 'nombre': answer[0][1]}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt), "nombre": answer[0][1], "rango": answer[0][3]}), 200     
            return jsonify({"Status": "Login incorrecto 22"}), 400
        return jsonify({"Status": "Login incorrecto 11"}), 400
    

class RegisterUserControllers(MethodView):
    def post(self):
        register = Register()
        content = request.get_json()
        nombre = content.get("nombre")
        correo = content.get("correo")
        contraseña = content.get("contraseña")
        salt = bcrypt.gensalt()
        register.contraseña = bcrypt.hashpw(bytes(str(contraseña), encoding= 'utf-8'), salt)
        register.nombre = nombre
        register.correo = correo
        message = register.add_user()

        return jsonify({"Status": "Registro ok",
                        "password_plano": contraseña}), 200
    


class HomeControllers(MethodView):

    def get(self):
        ga = Games()
        answer = ga.get_games()
        return jsonify(answer)

"""
class CarritoControllers(MethodView):

    def post(self):
        
        return jsonify({"hola"}), 200

    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email")}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403
    

class InicioVendedorControllers(MethodView):
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        correo = content.get("correo")
        contraseña = content.get("contraseña")

        return jsonify({"register ok": True, "correo": correo, "contraseña": contraseña}), 200

    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email")}), 200
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
        return jsonify({"Status": "No ha enviado un token"}), 403


class StockControllers(MethodView):
 
    def get(self):
        if (request.headers.get('Authorization')):
            token = request.headers.get('Authorization').split(" ")
            print("-----------------_", token[1])
            try:
                data = jwt.decode(token[1], KEY_TOKEN_AUTH , algorithms=['HS256'])
                return jsonify({"Status": "Autorizado por token", "emailextraido": data.get("email")})
            except:
                return jsonify({"Status": "TOKEN NO VALIDO"}), 403
            return jsonify({"Status": "No ha enviado un token"}), 403"""
     
