from models import conexion
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import conexion
import smtplib

class Register:
    def __init__(self):
        self.nombre = ''
        self.correo = ''
        self.contraseña = ''

    def add_user(self):
        res = conexion.Send('insert into usuarios (nombre,correo,password) values (%s, %s, %s)',[self.nombre,self.correo,self.contraseña])

    def gmail(self):
        proveedor_correo = 'smtp.live.com: 587'
        remitente = 'holamundopro@outlook.es'
        password = 'helloworld123'
        #conexion a servidor
        servidor = smtplib.SMTP(proveedor_correo)
        servidor.starttls()
        servidor.ehlo()
        #autenticacion
        servidor.login(remitente, password)
        #mensaje 
        mensaje = "<h1>Gracias por registrarte a Hello_game</h1>"
        msg = MIMEMultipart()
        msg.attach(MIMEText(mensaje, 'html'))
        msg['From'] = remitente
        msg['To'] = self.correo
        msg['Subject'] = 'Prueba'
        servidor.sendmail(msg['From'] , msg['To'], msg.as_string())


    def get_user(self):
        data = {}
        data['login'] = []
        res = conexion.Search("select * from usuarios where correo = %s ",[self.correo])
        return res