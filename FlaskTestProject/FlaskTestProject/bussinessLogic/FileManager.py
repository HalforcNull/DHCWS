import os
from FlaskTestProject import app
from FlaskTestProject.dataEntities import Result

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
        
    def __InitResult(self, resultFolder):
        dlist = os.listdir(resultFolder)
        myResult = Result.Result()
        for item in dlist:
            if item.startswith('title='):
                myResult.Title = item.replace('title=', '')
                continue
            if item.startswith('type='):
                myResult.Type = item.replace('type=', '')
                continue
            myResult.DataCount += 1
        return myResult
    
    def GetResults(self, taskId):
        resultList = []
        resultPath = OUTPUT_FILE_PATH + taskId +'/'
        if not os.path.exists(resultPath):
            return None

        try:
        
            rList = os.listdir(resultPath)
            for item in rList:
                try:
                    if os.path.isdir(resultPath+item):
                        #resultList.append(Result.Result())
                        resultList.append(self.__InitResult(resultPath+item))
                except Exception:
                    continue
        except Exception:
            return None
        return resultList

    def GetResultFileDirectory(self, taskId, resultId, fileId):
        fileFolderPath = OUTPUT_FILE_PATH + taskId + '/' + resultId + '/'
        files = os.listdir(fileFolderPath)
        for f in files:
            if f.rsplit('.',1)[0].lower() == fileId:
                return fileFolderPath + f
        else:
            return None

    def GetType(self, filepath):
        return filepath.rsplit('.', 1)[1].lower()
    