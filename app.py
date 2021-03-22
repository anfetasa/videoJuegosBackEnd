from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

from models.conexion import *

CORS(app, resources={r"/*": {"origins": "*"}})

from routes.routes import *

app.add_url_rule(user["register_user"], view_func=user["register_user_controllers"])
 
app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
# app.add_url_rule(user["Carrito_user"], view_func=user["Carrito"])
app.add_url_rule(user["home_user"], view_func=user["home"])

app.add_url_rule(user["stock_user"], view_func=user["stock"])

# vendedor

app.add_url_rule(admin["to_post"], view_func=admin["topost"])



if __name__ == '__main__':
    app.run(debug=True,port=5000)

