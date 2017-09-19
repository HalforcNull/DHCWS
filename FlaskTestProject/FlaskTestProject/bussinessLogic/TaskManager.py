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
        print(args)
        print(result_args)
        cursor.close()
        conn.close()
        return result_args[2]
