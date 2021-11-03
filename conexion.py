print ("Resultados de mysql.connector:")
import mysql.connector
miConexion = mysql.connector.connect( host='localhost', user= 'root', passwd='admin', db='sys' )
cur = miConexion.cursor()
cur.execute( "SELECT nombre, ciudad FROM clientes" )
for nombre, ciudad in cur.fetchall() :
    print (nombre, ciudad)
miConexion.close()