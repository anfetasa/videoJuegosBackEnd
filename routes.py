from controllers import LoginUserControllers, RegisterUserControllers , InicioVendedorControllers,CarritoControllers,HomeControllers


user = {
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "register_user": "/api/v01/user/register", "register_user_controllers": RegisterUserControllers.as_view("register_api"),
    "Carrito_user": "/api/v01/user/carrito", "Carrito": CarritoControllers.as_view("Carrito_api"),
    "home_user": "/api/v01/user/home", "home": HomeControllers.as_view("home_api")
}


vendedor = {
    "vendedor_api": "/api/v01/vendedor/login", "login_vendedor_controllers": InicioVendedorControllers.as_view("vendedor_api"),
}