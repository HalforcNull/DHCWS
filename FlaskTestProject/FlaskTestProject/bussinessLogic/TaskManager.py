from FlaskTestProject.dataEntities import DataAccess

class TaskManager:
    def __init__(self):
        self.DataAccess = DataAccess.DataAccess()
        return
    
    def getNewTask(self, scriptID, userID):
        return self.DataAccess.CreateNewTask(scriptID, userID)

    def activeTask(self, taskID):
        return self.DataAccess.ActiveTask(taskID)

    def updateTaskParms(self, taskId, parmValues):
        self.DataAccess.UpdateTaskParms(taskId, parmValues)
        return

    def getFirstPendingTask(self, serverName):
        return self.DataAccess.GetFirstPendingTask(serverName)

    def checkinTask(self, serverName):
        self.DataAccess.CheckinTask(serverName)
        return