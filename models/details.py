from models import conexion

class Details:
    def __init__(self):
        self.id = 0

    def GetDetails(self):
        data = {}
        data['videojuegos'] = []
        res = conexion.Search("select * from videojuegos where id = %s ",[self.id])
        print(res)
        for i in res:
            data['videojuegos'].append({'id':i[0],'nombre':i[1],'descripcion':i[3],'precio':i[4],'categoria':i[5]})
        return data['videojuegos'] 