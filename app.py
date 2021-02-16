from flask import Flask
from routes import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["register_user"], view_func=user["register_user_controllers"])
app.add_url_rule(user["Carrito_user"], view_func=user["Carrito"])
app.add_url_rule(user["home_user"], view_func=user["home"])

# vendedor

app.add_url_rule(vendedor["vendedor_api"], view_func=vendedor["login_vendedor_controllers"])
