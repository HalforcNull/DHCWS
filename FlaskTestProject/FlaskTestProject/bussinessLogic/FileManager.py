import os
from FlaskTestProject import app

UPLOAD_FOLDER = app.config['ENV_FILE_UPLOAD_FOLDER']
OUTPUT_FILE_PATH = app.config['ENV_OUTPUT_FILE_PATH']
ALLOWED_EXTENSIONS = app.config['CONFIG_ALLOWED_EXTENSIONS']

class FileManager:
    #private method
    #this will change if we allowed more types of file
    #allowed file types should be listed for each script in tblscripts table
    def __allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    #public method
    def UploadFileForGivenTask(self, file, taskId, fileId):
        if file.filename =='':
            return 'No File Selected'
        if not self.__allowed_file(file.filename):
            return 'Not correct format'
        if not file:
            return 'Not file error'
        directory = UPLOAD_FOLDER + taskId + '/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = fileId + '.' + file.filename.rsplit('.',1)[1].lower()
        file.save(directory+filename)
        return 'Success'
    
    def GetRScriptRunningEnvPath(self):
        # we only support R now
        return app.config['ENV_RSCRIPT_RUNNING_ENV_PATH']
    
    def GetRExeRunningEnvPath(self):
        return app.config['ENV_REXE_ENV_PATH']

    def GetTaskInputFolder(self, taskId):
        return app.config['ENV_INPUT_FILE_PATH'] + str(taskId) + '/'

    def GetTaskOutputFolder(self, taskId):
        return app.config['ENV_OUTPUT_FILE_PATH'] + str(taskId) + '/'

    def GetScriptLocation(self, scriptId):
        slist = os.listdir( app.config['ENV_SCRIPTFOLDER'] )
        for scriptFileName in slist:
            if scriptFileName.rsplit('.',1)[0].lower() == str(scriptId):
                return app.config['ENV_SCRIPTFOLDER'] + scriptFileName
        raise FileNotFoundError()
        
    
    def GetResults(self, taskId):
        try:
            rList = os.listdir(path=OUTPUT_FILE_PATH + taskId +'/')
            return rList
        except Exception:
            return None
    
    def GetResultFileDirectory(self, taskId, fileId):
        fl = self.GetResults(taskId)
        if fl is None:
            return None
        for filename in fl:
            if fileId in filename:
                return OUTPUT_FILE_PATH + taskId + '/' + filename
    
    def GetType(self, filepath):
        return filepath.rsplit('.', 1)[1].lower()
    