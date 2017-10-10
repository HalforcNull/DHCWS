import subprocess
import time

import mysql.connector
from pip._vendor import requests
import EnvironmentData
import TaskData
import Config

#TODO: CONFIG

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'dbo'

TASKCHECKINTERVAL = 30
ENVCHECKINTERVAL = 30
SERVERNAME = 'Runner1'

def checkOutNewTask(LoadBalanceServerAddress):
    """ check if there any new task assigned to current runner"""
    url = LoadBalanceServerAddress+'/api/requestnewtask/'+ SERVERNAME
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    print(response.text)
    return ''

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
    # should set task to running =
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
    print('Checking Environment')
    envData = EnvironmentData.EnviromentData()
    
    envData.LoadBalanceServerAddress = getLoadBalancerServer()
    envData.IsGood = envData.IsGood and envData.LoadBalanceServerAddress != ''
    
    return envData

def queryTask(envData):
    raise NotImplementedError()

def pullFilesIntoEnviroment(envData):
    """not this time"""
    return

def buildCommand(envData, taskData):
    options = {
        TaskData.TaskType.RScript: RScriptCommandGenerater,
        TaskData.TaskType.RMarkDown: RMarkdownCommandGenerater,
        TaskData.TaskType.Unknown: UnknownScriptCommand
    }
    CommandBulder = options.get(taskData.TaskType, default = UnknownScriptCommand)
    return CommandBulder(envData, taskData)


def RMarkdownCommandGenerater(envData, taskData):
    return envData.R_EXE_PATH + ' -e "rmarkdown::render(\'' + envData.Script_PATH + \
            taskData.ScriptId + '.rmd, output_file=\'result.html\')" ' + \
            '--args --inputfolder=\''

def RScriptCommandGenerater(envData, taskData):
    raise NotImplementedError()

def UnknownScriptCommand(envData, taskData):
    print('Unknown Script Type Detected. Script ID:' + taskData.ScriptId)
    return ''

def pushResultIntoDataCenter(envData, taskData):
    """not this time"""
    return

def checkInTask(envData, taskData):
    #we may need task id later
    url = envData.LoadBalanceServerAddress +'/api/checkinassignedtask/' + SERVERNAME
    requests.post(url)
    return

def SetScriptToActive(envData, taskData):
    #TODO
    return 


if __name__ == '__main__':
    EnvData = envCheck()
    while EnvData.IsGood != True:
        time.sleep(ENVCHECKINTERVAL)
        EnvData = envCheck()

    print('Get load balance server with ip: ' + EnvData.LoadBalanceServerAddress)

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
    
    #if Config.Config().FILE_MOVE_REQUIRED
    if False:
        while True:
            Task = queryTask(EnvData)
            if Task is None:
                time.sleep(TASKCHECKINTERVAL)
                continue
            
            pullFilesIntoEnviroment(EnvData)

            TaskCommand = buildCommand(EnvData, Task)
            if TaskCommand == '':
                time.sleep(TASKCHECKINTERVAL)
                continue
            
            SetScriptToActive(EnvData, Task)
            RunScript(TaskCommand)

            pushResultIntoDataCenter(EnvData, Task)

            checkInTask(EnvData, Task)

            time.sleep(TASKCHECKINTERVAL)
    else:    
        while True:
            TaskCommand = ''
            try:
                TaskCommand = checkOutNewTask(EnvData.LoadBalanceServerAddress)
            except Exception as e:
                print('Error occur when connecting to Web Server:' + EnvData.LoadBalanceServerAddress )

            if TaskCommand != '':
                RunScript(TaskCommand)
            else:
                print('No Task Command')
            
