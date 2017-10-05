import subprocess
import time

import mysql.connector
from pip._vendor import requests
import EnvironmentData

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


def getLoadBalancerServer():
    LoadBalanceServerAddress = ''
    try:
        LoadBalanceServerAddress = getBalanceServer()
    except Exception as e:
        print('Error occur when connecting to Database. ')
    
    return LoadBalanceServerAddress
    


def envCheck():
    envData = EnvironmentData.EnviromentData()
    isGoodToWork = False
    envData.LoadBalanceServerAddress = getLoadBalancerServer()
    if envData.LoadBalanceServerAddress == '':
        isGoodToWork = True
    
    envData.
    return isGoodToWork

if __name__ == '__main__':
    """ THIS IS NOT THE FINAL SOLUTION 
        Command should be built in script runner.
        All env parm should managed by script runner
        Load Balancer only need pass script id, task id, and regular parms.
        Script Runner need:
        1. query task, query config
        2. pull files into its environment (script and input file)
        3. built the command
        4. set task 'running' flag = true and run the command.
        5. get result, push data back to data center/file center
        6. check in task """

    print('Checking Environment')
    EnvData = EnvironmentData.EnviromentData()
    LoadBalanceServerAddress = ''


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
