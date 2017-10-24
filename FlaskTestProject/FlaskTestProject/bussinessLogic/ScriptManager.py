import mysql.connector
from FlaskTestProject.dataEntities import Script
from FlaskTestProject.dataEntities import DataAccess
from FlaskTestProject import DesignPatterns
import json

class ScriptManager(DesignPatterns.Singleton):

    def __init__(self):
        self.DataAccess = DataAccess.DataAccess()
        return

    def getScriptIDbyName(self, scriptName):
        #TODO
        #Do we need it????
        raise NotImplementedError()

    def getScriptExecuteablePath(self, scriptId):
        raise NotImplementedError('getScriptExecuteablePath not impletemented yet')

    def getScriptList(self):
        return self.DataAccess.GetSctriptList()

    def getInputFileRequirementListbyId(self, scriptId):
        raise NotImplementedError()
    
    def getInputFileListbyId(self, scriptId):
        raise NotImplementedError('getInputFileListbyId not impletemented yet')

    def getInputParmRequirementLIstbyId(self, scriptId):
        raise NotImplementedError()

    def getInputFileDescription(self, scriptId, fileId):
        raise NotImplementedError()

    def getInputParmDescription(self, scriptId, parmId):
        raise NotImplementedError()
