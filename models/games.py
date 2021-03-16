from models import conexion

class Games:
    def __init__(self):
        self.nombre = ''
        self.descripcion = ''
        self.precio = ''
        self.categoria = ''

    def get_games(self):
        data = {}
        data['videojuegos'] = []
        res = conexion.View("select id, nombre, categoria from videojuegos")
        for i in res:
            data['videojuegos'].append({'id':i[0],'nombre':i[1],'categoria':i[2]})
        return data['videojuegos']