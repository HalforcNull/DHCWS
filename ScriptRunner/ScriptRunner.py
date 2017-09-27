import subprocess
import time

import mysql.connector
from pip._vendor import requests

#TODO: CONFIG

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'dbo'

SLEEPINTERVAL = 30
SERVERNAME = 'Runner 1'


if __name__ == '__main__':
    print('Runner start')
    LoadBalanceServerAddress = getBalanceServer()
    while True:
        if LoadBalanceServerAddress == '':
            print('no load balance server founded.')
        time.sleep(SLEEPINTERVAL)

    print('Get load balance server with ip: ' + LoadBalanceServerAddress)

    while True:
        TaskCommand = checkOutNewTask()
        if TaskCommand != '':
            subprocess.call(TaskCommand, shell=False)
            checkInTask()
            # no error handling code
        time.sleep(SLEEPINTERVAL)



def checkOutNewTask():
    """ check if there any new task assigned to current runner"""
    url = LoadBalanceServerAddress+'/api/requestnewtask/'+ SERVERNAME
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    print(response.text)
    return ''

def checkInTask():
    url = LoadBalanceServerAddress+'/api/requestnewtask/' + SERVERNAME
    requests.post(url)
    return

def regServer():
    args = (SERVERNAME, '' , '' , 'Script Runner')
    conn = mysql.connector.connect( host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE )
    cursor = conn.cursor()
    cursor.callproc('spRegServer',args)
    cursor.close()
    conn.commit()
    conn.close()

def getBalanceServer():
    args = (0)
    conn = mysql.connector.connect( host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE )
    cursor = conn.cursor()
    result_args = cursor.callproc('spGetLoadBalanceServer',args)
    cursor.close()
    conn.commit()
    conn.close()
    return result_args[0]
