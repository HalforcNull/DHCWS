import  mysql.connector
from FlaskTestProject.dataEntities import Script
from FlaskTestProject.dataEntities import Task
from FlaskTestProject import app

class DataAccess:
    __HOSTNAME__ = app.config['DB_HOSTNAME']
    __USERNAME__ = app.config['DB_USERNAME']
    __PASSWORD__ = app.config['DB_PASSWORD']
    __DATABASE__ = app.config['DB_DATABASE']

    def __callStoredProcedure(self, spname, spargs):
        """ call SP based on the spname. spargs should incloud space for output args
            The returned args need to be explained by case"""

        conn = mysql.connector.connect( host=self.__HOSTNAME__, user=self.__USERNAME__, 
                                        passwd=self.__PASSWORD__, db=self.__DATABASE__ )
        cursor = conn.cursor()
        result_args = cursor.callproc(spname, spargs)
        cursor.close()
        conn.commit()
        conn.close()
        return result_args

    def __fetchallFromStoredProcedure(self, spname, spargs=None):

        conn = mysql.connector.connect( host=self.__HOSTNAME__, user=self.__USERNAME__, 
                                        passwd=self.__PASSWORD__, db=self.__DATABASE__ )
        cursor = conn.cursor()
        if spargs is None:
            cursor.callproc(spname)
        else:
            cursor.callproc(spname, spargs)

        for result in cursor.stored_results():
            queryResult = result.fetchall()

        cursor.close()
        conn.commit()
        conn.close()
        return queryResult

    def CreateNewTask(self, scriptID, userID):
        """ create a new task for user, script need to be specified """
        args = (scriptID, userID, 0)
        result = self.__callStoredProcedure('spCreateNewTask',args)
        return result[2]

    def ActiveTask(self, taskID):
        """ active a task """
        args = (taskID, 0)
        result = self.__callStoredProcedure('spActiveTask', args)
        return result[1]

    def UpdateTaskParms(self, taskID, parmValues):
        """ update parms of a task """
        args = (taskID, " ".join(parmValues))
        self.__callStoredProcedure('spUpdateTaskParms',args)
        return

    def GetSctriptList(self):
        fetchallResult = self.__fetchallFromStoredProcedure('spGetScriptList')
        scriptList = []

        for scriptInfo in fetchallResult:
            scriptList.append( Script.Script(scriptInfo[0], scriptInfo[1], scriptInfo[2]) )

        return scriptList

    def GetFirstPendingTask(self, servername):
        """ get the first pending task. if no task pending return none """
        args = (servername,)
        fetchallResult = self.__fetchallFromStoredProcedure('spGetPendingTask',args)
        if len(fetchallResult) < 1:
            return None
        for taskInfo in fetchallResult:
            return Task.Task(taskInfo[0],taskInfo[1],taskInfo[2],taskInfo[3])
    
    def CheckinTask(self, servername):
        args = (servername,)
        self.__callStoredProcedure('spCheckinTask', args)
        return

    def AssignMostOldUnsignedTask(self, servername):
        """ this is not the correct way, demo only """
        args = (servername,)
        self.__callStoredProcedure('spDemoOnlyAssignTask', args)
        return
