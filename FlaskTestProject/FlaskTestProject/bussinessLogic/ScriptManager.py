import mysql.connector
from FlaskTestProject.dataEntities import Script
from FlaskTestProject.dataEntities import DataAccess
import json

#TODO: CONFIG 
hostname = 'localhost'
username = 'root'
password = 'root'
database = 'dbo'

class ScriptManager:

    def __init__(self):
        self.DataAccess = DataAccess.DataAccess()
        return

    def getScriptIDbyName(self, scriptName):
        #TODO
        #Do we need it????
        return 1
    def getScriptExecuteablePath(self, scriptId):
        raise NotImplementedError('getScriptExecuteablePath not impletemented yet')
    def getScriptList(self):
        return self.DataAccess.GetSctriptList()

    def getInputFileRequirementListbyId(self, scriptId):
        return 1
    
    def getInputFileListbyId(self, scriptId):
        raise NotImplementedError('getInputFileListbyId not impletemented yet')
    def getInputParmRequirementLIstbyId(self, scriptId):
        return 1
    def getInputFileDescription(self, scriptId, fileId):
        return 1
    def getInputParmDescription(self, scriptId, parmId):
        return 1


