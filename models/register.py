from models import conexion

class Register:
    def __init__(self):
        self.nombre = ''
        self.correo = ''
        self.contraseña = ''

    def add_user(self):
        res = conexion.Send('insert into usuarios (nombre,correo,password) values (%s, %s, %s)',[self.nombre,self.correo,self.contraseña])

    def get_user(self):
        data = {}
        data['login'] = []
        res = conexion.Search("select * from usuarios where correo = %s ",[self.correo])
        return res