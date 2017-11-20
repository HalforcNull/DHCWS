"""
This script runs the FlaskTestProject application using a development server.
"""

from os import environ
from FlaskTestProject import app
import mysql.connector

#TODO: CONFIG 
hostname = 'localhost'
username = 'root'
password = 'root'
database = 'dbo'


"""this is my local server run script
"""
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    args = ('WebServer', HOST, PORT, 'FN')
    
    conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
    cursor = conn.cursor()
    cursor.callproc('spRegServer',args)
    cursor.close()
    conn.commit()
    conn.close()

    app.run(HOST, PORT)

