from FlaskTestProject.bussinessLogic import ( TaskManager, ScriptManager, FileManager )
from FlaskTestProject.dataEntities import Task
from FlaskTestProject import app


class LoadBalancer:
    def __init__(self):
        self.TaskManager = TaskManager.TaskManager()
        self.FileManager = FileManager.FileManager()


    def getPendingTaskCommand(self, serverName):
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
              

        PendingTask = self.TaskManager.getFirstPendingTask(serverName)
        if PendingTask is None:
            return ''
        
        CommandString = ' '.join((
            self.FileManager.GetRScriptRunningEnvPath(),
            self.FileManager.GetScriptLocation(PendingTask.ScriptId),
            PendingTask.Parm))
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
