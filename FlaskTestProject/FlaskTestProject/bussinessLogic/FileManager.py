import os

#TODO LATER: MOVE THESE PARMS INTO CONFIG?
UPLOAD_FOLDER = 'c:/FlaskTestProject/Data/user/uploadfiles/'
ALLOWED_EXTENSIONS = set(['csv'])


class FileManager:
    #private method
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
            
            #return 'Success'
