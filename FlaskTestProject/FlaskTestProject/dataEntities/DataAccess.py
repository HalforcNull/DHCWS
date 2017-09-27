import  mysql.connector

class DataAccess:
    __HOSTNAME__ = 'localhost'
    __USERNAME__ = 'root'
    __PASSWORD__ = 'root'
    __DATABASE__ = 'dbo'

    def __callStoredProcedure__(self, spname, spargs):
        """ call SP based on the spname. spargs should incloud space for output args
            The returned args need to be explained by case"""

        conn = mysql.connector.connect( host=self.__HOSTNAME__, user=self.__USERNAME__, passwd=self.__PASSWORD__, db=self.__DATABASE__ )
        cursor = conn.cursor()
        result_args = cursor.callproc(spname, spargs)
        cursor.close()
        conn.commit()
        conn.close()
        return result_args

    def CreateNewTask(self, scriptID, userID):
        """ create a new task for user, script need to be specified """
        args = (scriptID, userID, 0)
        result = self.__callStoredProcedure__('spCreateNewTask',args)
        return result[2]

    def ActiveTask(self, taskID):
        """ active a task """
        args = (taskID, 0)
        result = self.__callStoredProcedure__('spActiveTask', args)
        return result[1]

    def UpdateTaskParms(self, taskID, parmValues):
        """ update parms of a task """
        args = (taskID, " ".join(parmValues))
        self.__callStoredProcedure__('spUpdateTaskParms',args)
        return
