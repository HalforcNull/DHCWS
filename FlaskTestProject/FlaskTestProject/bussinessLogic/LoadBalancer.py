from FlaskTestProject.bussinessLogic import ( TaskManager, ScriptManager)
from FlaskTestProject.dataEntities import Task


RRUNNIGPATH = 'C:/Program Files/R/R-3.4.1/bin/RScript.exe'
SCRIPTFOLDER = 'C:/DemoScriptFolder/'
WORKINGPATH = 'C:/WorkingPath/'
INPUTSUBPATH = '/Inputs/'
OUTPUTSUBPATH = '/Outputs/'

class LoadBalancer:
    def __init__(self):
        self.TaskManager = TaskManager.TaskManager()


    def getPendingTaskCommand(self, serverName):
        PendingTask = self.TaskManager.getFirstPendingTask(serverName)
        if PendingTask is None:
            return ''
        
        CommandString = RRUNNIGPATH + ' ' + SCRIPTFOLDER + str(PendingTask.ScriptId) + '.R' + ' ' + PendingTask.Parm # + ' ' 
        #+ WORKINGPATH+PendingTask.TaskId+OUTPUTSUBPATH + ' '
        # work output path is the first parm of any script
        #+ WORKINGPATH+PendingTask.TaskId+OUTPUTSUBPATH + PendingTask.
        # It should be :
        # execParms =  getInputParms()+ getOutputParms()
        # CommandString = ' '.Join( (Config.GetRScriptPath(),) + ( ScriptManager.getScriptExecuteablePath(PendingTask.ScriptId),) + execParms )
        return CommandString

    def __getInputParms(self, taskId, scriptId, taskParms):
        
        InputPath = WORKINGPATH + taskId + INPUTSUBPATH
        filesParm = InputPath.join( ScriptManager.ScriptManager.getInputFileListbyId(taskId, scriptId) )
        
        if filesParm == '':
            return taskParms
        else:
            return filesParm + ' ' + taskParms
