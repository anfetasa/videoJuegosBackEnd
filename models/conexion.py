from flask_mysqldb import MySQL
from app import app

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PASSWORD']='Radamelcafetero23009'
app.config['MYSQL_USER']='root'
app.config['MYSQL_DB']='videojuegos'        

mysql = MySQL(app) 

def Send(sql, valor): 
    curs = mysql.connection.cursor()
    curs.execute(sql,valor)
    mysql.connection.commit()
    curs.close()
    return("Se ha agregado correctamente")

def View(sql):
    curs = mysql.connection.cursor()
    curs.execute(sql)
    Data = curs.fetchall()
    curs.close()
    return Data 

def Search(sql,valor):
        curs = mysql.connection.cursor()
        curs.execute(sql,valor)
        Data = curs.fetchall()
        curs.close()
        return Data

def SearchAdmin(sql):
        curs = mysql.connection.cursor()
        curs.execute(sql)
        Data = curs.fetchall()
        curs.close()
        return Data
    