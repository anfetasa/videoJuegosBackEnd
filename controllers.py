
from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        correo = content.get("correo")
        contraseña = content.get("contraseña")
        print(correo)
        return jsonify({"register ok": True, "correo": correo, "contraseña": contraseña}), 200
    

class RegisterUserControllers(MethodView):

    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        nombre = content.get("nombre")
        correo = content.get("correo")
        contraseña = content.get("contraseña")

        return jsonify({"register ok": True, "nombre": nombre, "correo": nombre, "contraseña": contraseña}), 200
        print(nombre, correo)
    


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


    def get():
        pass
    
    def put():
        pass
     
