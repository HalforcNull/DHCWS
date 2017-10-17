from FlaskTestProject.bussinessLogic import ( TaskManager, ScriptManager, FileManager )
from FlaskTestProject.dataEntities import ( Task, DataAccess )
from FlaskTestProject import app


class LoadBalancer:
    def __init__(self):
        self.TaskManager = TaskManager.TaskManager()
        self.FileManager = FileManager.FileManager()
        self.DataAccess = DataAccess.DataAccess()

    def __assignNewTaskToServer(self, serverName):
        self.DataAccess.AssignMostOldUnsignedTask(serverName)
        return

    """
    def __getInputParms(self, taskId, scriptId, taskParms):
        InputPath = app.config['ENV_INPUT_FILE_PATH'] + taskId
        #filesParm = InputPath.join( ScriptManager.ScriptManager.getInputFileListbyId(taskId, scriptId) )
        
        return InputPath + ' ' + taskParms
    """

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
            self.__assignNewTaskToServer(serverName)
        
        PendingTask = self.TaskManager.getFirstPendingTask(serverName)
        if PendingTask is None:
            return ''
        
        if PendingTask.Parm is None:
            PendingTask.Parm = ''

        scriptfile = self.FileManager.GetScriptLocation(PendingTask.ScriptId)
        if self.FileManager.GetType(scriptfile) == 'r':    
            CommandString = ' '.join((
                self.FileManager.GetRScriptRunningEnvPath(),
                self.FileManager.GetScriptLocation(PendingTask.ScriptId),
                self.FileManager.GetTaskInputFolder(PendingTask.TaskId),
                self.FileManager.GetTaskOutputFolder(PendingTask.TaskId),
                PendingTask.Parm))
        else:
            CommandString = ' '.join((
                self.FileManager.GetRExeRunningEnvPath(),
                '-e',
                '"rmarkdown::render(\'' + self.FileManager.GetScriptLocation(PendingTask.ScriptId) + 
                    '\', output_file=\'' + self.FileManager.GetTaskOutputFolder(PendingTask.TaskId) + '0.html\')"',
                '--args',
                '--inputFolder="' + self.FileManager.GetTaskInputFolder(PendingTask.TaskId) + '"',
                '--outputFolder="' + self.FileManager.GetTaskOutputFolder(PendingTask.TaskId) + '"'
            ))
        #+ WORKINGPATH+PendingTask.TaskId+OUTPUTSUBPATH + ' '
        # work output path is the first parm of any script
        #+ WORKINGPATH+PendingTask.TaskId+OUTPUTSUBPATH + PendingTask.
        # It should be :
        # execParms =  getInputParms()+ getOutputParms()
        # CommandString = ' '.Join( (Config.GetRScriptPath(),) + ( ScriptManager.getScriptExecuteablePath(PendingTask.ScriptId),) + execParms )
        return CommandString




