"""
This script runs the FlaskTestProject application using a development server.
"""

from os import environ
from FlaskTestProject import app
import mysql.connector


"""this is my local server run script
"""
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', app.config['WEB_HOSTIP'])
    try:
        PORT = int(environ.get('SERVER_PORT', app.config['WEB_PORT']))
    except ValueError:
        PORT = app.config['WEB_BACKUPPORT']

    try:
        args = ('WebServer', HOST, PORT, 'FN')    
        conn = mysql.connector.connect( host=app.config['DB_HOSTNAME'], user=app.config['DB_USERNAME'], passwd=app.config['DB_PASSWORD'], db=app.config['DB_DATABASE'] )
        cursor = conn.cursor()
        cursor.callproc('spRegServer',args)
        cursor.close()
        conn.commit()
        conn.close()
    except Exception:
        print('Error occur when register web server to DB. Web sever may lose some function.')

    app.run(HOST, PORT, use_reloader=False)

