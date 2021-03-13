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
        res = conexion.View("select nombre, categoria from videojuegos")
        for i in res:
            data['videojuegos'].append({'nombre':i[0],'categoria':i[1]})
        return data['videojuegos']