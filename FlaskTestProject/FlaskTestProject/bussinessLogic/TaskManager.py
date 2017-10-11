from FlaskTestProject.dataEntities import DataAccess
from FlaskTestProject.bussinessLogic import FileManager

class TaskManager:
    def __init__(self):
        self.DataAccess = DataAccess.DataAccess()
        return
    
    def getNewTask(self, scriptID, userID):
        return self.DataAccess.CreateNewTask(scriptID, userID)

    def activeTask(self, taskID):
        """ current code is for demo only
        the fully workflow is :
        1. get request id
        2. check every required files in 'input' folder
        3. check parms ---??
        4. active task
        """
        return self.DataAccess.ActiveTask(taskID)

    def updateTaskParms(self, taskId, parmValues):
        self.DataAccess.UpdateTaskParms(taskId, parmValues)
        return

    def getFirstPendingTask(self, serverName):
        return self.DataAccess.GetFirstPendingTask(serverName)
    
    def checkinTask(self, serverName):
        self.DataAccess.CheckinTask(serverName)
        return
    
    def taskContainsHtmlResult(self, taskId):
        filemanager = FileManager.FileManager()
        fileList = filemanager.GetResults(taskId)
        if fileList is None:
            return False

        for filename in fileList:
            if '.' in filename and filename.rsplit('.', 1)[1].lower() == 'html':
                return True
        
    def GetResultList(self, taskId):
        filemanager = FileManager.FileManager()
        fileList = filemanager.GetResults(taskId)
        return fileList 

