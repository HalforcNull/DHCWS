from FlaskTestProject.dataEntities import DataAccess
from FlaskTestProject.bussinessLogic import FileManager
from FlaskTestProject import DesignPatterns
import os

class TaskManager(DesignPatterns.Singleton):
    DataAccess = None
    def __init__(self):
        if self.DataAccess is None:
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
        outputfolder = filemanager.GetTaskOutputFolder(taskId)
        fileList = os.listdir(outputfolder)
        if fileList is None:
            return False

        for filename in fileList:
            if '.' in filename and filename.rsplit('.', 1)[1].lower() == 'html':
                return True
        
    def GetResultList(self, taskId):
        filemanager = FileManager.FileManager()
        fileList = filemanager.GetResults(taskId)
        return fileList 


