from models import conexion

class Details:
    def __init__(self):
        self.id = 0

    def GetDetails(self):
        data = {}
        data['videojuegos'] = []
        res = conexion.Search("select * from videojuegos where id = %s ",[self.id])
        for i in res:
            data['videojuegos'].append({'id':i[0],'nombre':i[1],'descripcion':i[2],'precio':i[3],'categoria':i[4]})
        print (data['videojuegos'])
        return data['videojuegos'] 
        