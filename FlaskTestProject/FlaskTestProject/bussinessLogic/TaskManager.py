import mysql.connector

#TODO: CONFIG 
hostname = 'localhost'
username = 'root'
password = 'root'
database = 'dbo'

class TaskManager:
    def getNewTask(self, scriptID, userID):
        returnedTaskID = ''
        conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
        cursor = conn.cursor()
        #try:
        args = (scriptID, userID, 0)
        result_args = cursor.callproc('spCreateNewTask',args)
        #    returnedTaskID = result_args[1]

        #except Error as e:
        #    print(e)

        #finally:
        
        cursor.close()
        conn.commit()
        conn.close()
        return result_args[2]

    def activeTask(self, taskID):
        conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
        cursor = conn.cursor()

        args=(taskID, 0)
        result_args = cursor.callproc('spActiveTask',args)
        cursor.close()
        conn.commit()
        conn.close()
        return result_args[1]

    def updateTaskParms(self, taskId, parmValues):
        conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
        cursor = conn.cursor()

        args = (taskId, " ".join(parmValues))
        cursor.callproc('spUpdateTaskParms',args)
        cursor.close()
        conn.commit()
        conn.close()
        return

