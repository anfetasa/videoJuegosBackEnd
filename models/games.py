from models import conexion

class Games:
    def __init__(self):
        self.nombre = ''
        self.descripcion = ''
        self.precio = ''
        self.categoria = ''
        self.img = ''
        self.idUsuario = ''
        self.idJuego = ''
        self.correo = ''
        self.juegos = ''

    def add_games(self):
        res = conexion.Send('insert into videojuegos (nombre, descripcion, precio, categoria, img) values (%s, %s, %s, %s, %s)',[self.nombre,self.descripcion,self.precio,self.categoria,self.img])

    def get_games(self):
        data = {}
        data['videojuegos'] = []
        res = conexion.View("select id, nombre, categoria, img from videojuegos")
        for i in res:
            data['videojuegos'].append({'id':i[0],'nombre':i[1],'categoria':i[2], 'img':i[3]})
        return data['videojuegos']

    def add_carrito(self):
        res = conexion.Send('insert into carrito (idUsuario, idJuego) values (%s, %s)',[self.idUsuario, self.idJuego])

    def get_games_carrito(self):
        data = {}
        data['videojuegos'] = []
        res = conexion.View("select v.id, v.nombre, v.precio, v.img, c.id from videojuegos v, carrito c where v.id = c.idJuego and c.idUsuario = '{}'".format(self.correo))
        for i in res:
            data['videojuegos'].append({'id':i[0], 'nombre':i[1], 'precio':i[2], 'img':i[3], 'idRegistro':i[4]})
        return data['videojuegos']

    def delete_carrito(self):
        res = conexion.Send("delete from carrito where id = %s and idUsuario = %s",[self.idJuego, self.correo])

    def delete_All_carrito(self):
         res = conexion.Send("delete from carrito where idUsuario = %s",[self.correo])

    def registro_compras(self):

        for item in self.juegos:
            res = conexion.Send("insert into registro_compra (idUsuario, idJuego) values (%s, %s)", [self.correo, item["id"]])

    
