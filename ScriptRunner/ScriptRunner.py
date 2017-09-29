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
SERVERNAME = 'Runner1'

def checkOutNewTask():
    """ check if there any new task assigned to current runner"""
    url = LoadBalanceServerAddress+'/api/requestnewtask/'+ SERVERNAME
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    print(response.text)
    return ''

def checkInTask():
    #we may need task id later
    url = LoadBalanceServerAddress+'/api/checkinassignedtask/' + SERVERNAME
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
    return

def getBalanceServer():
    args = (0,0)
    conn = mysql.connector.connect( host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE )
    cursor = conn.cursor()
    result_args = cursor.callproc('spGetLoadBalancerServer',args)
    cursor.close()
    conn.commit()
    conn.close()
    return 'http://'+result_args[0]+':'+result_args[1]

def RunScript(cmd):
    print('Start Command: ')
    print(TaskCommand)
    return
    # subprocess.call(TaskCommand, shell=False)
    # checkInTask()
    # no error handling code


if __name__ == '__main__':
    print('Runner start')
    LoadBalanceServerAddress = ''
    try:
        LoadBalanceServerAddress = getBalanceServer()
    except Exception as e:
        print('Error occur when connecting to Database. ')
    
    while LoadBalanceServerAddress == '':
        print('no load balance server founded.')
        time.sleep(SLEEPINTERVAL)

    print('Get load balance server with ip: ' + LoadBalanceServerAddress)

    while True:
        TaskCommand = ''
        try:
            TaskCommand = checkOutNewTask()
        except Exception as e:
            print('Error occur when connecting to Web Server:' + LoadBalanceServerAddress )

        if TaskCommand != '':
            RunScript(TaskCommand)
        else:
            print('No Task Command')

        time.sleep(SLEEPINTERVAL)
