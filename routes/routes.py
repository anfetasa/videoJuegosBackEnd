from controllers.controllers import RegisterUserControllers, LoginUserControllers, HomeControllers, StockControllers, ToPostControllers, CarritoControllers, CarritoStockControllers, BuyStockControllers, RegistroCompraControllers


user = {
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "register_user": "/api/v01/user/register", "register_user_controllers": RegisterUserControllers.as_view("register_api"),
    "Carrito_user": "/api/v01/user/carrito", "Carrito": CarritoControllers.as_view("Carrito_api"),
    "home_user": "/api/v01/user/home", "home": HomeControllers.as_view("home_api"),
    "stock_user": "/api/v01/user/stock/<id>", "stock": StockControllers.as_view("stock_api"),
    "CarritoStock_user": "/api/v01/user/carritoStock/<id>/<token>", "CarritoStock": CarritoStockControllers.as_view("CarritoStock_api"),
    "buyStock_user": "/api/v01/user/buyStock", "buyStock": BuyStockControllers.as_view("buyStock_api"),
    "registroCompra_user": "/api/v01/user/registroCompra/<id>/<token>", "registroCompra": RegistroCompraControllers.as_view("registroCompra_api"),
}

 
admin = {
    "to_post": "/api/v01/admin/topost", "topost": ToPostControllers.as_view("admin_api"),
}