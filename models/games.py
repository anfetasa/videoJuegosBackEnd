from models import conexion

class Games:
    def __init__(self):
        self.nombre = ''
        self.descripcion = ''
        self.precio = ''
        self.categoria = ''
        self.img = ''

    def get_games(self):
        data = {}
        data['videojuegos'] = []
        res = conexion.View("select id, nombre, categoria, img from videojuegos")
        for i in res:
            data['videojuegos'].append({'id':i[0],'nombre':i[1],'categoria':i[2], 'img':i[3]})
        return data['videojuegos']