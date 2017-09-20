import mysql.connector
from FlaskTestProject.dataEntities import Script
import json

#TODO: CONFIG 
hostname = 'localhost'
username = 'root'
password = 'root'
database = 'dbo'

class ScriptManager:
    def getScriptIDbyName(self, scriptName):
        #TODO
        #Do we need it????
        return 1

    def getScriptList(self):
        conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
        cursor = conn.cursor()
        cursor.callproc('spGetScriptList')
        ScriptList = []
        
        #return [(1, 'DemoScript1', None), (2, 'DemoScript2', None), (3, 'DemoScript3', None), (4, 'R notebook on DESeq2', None)]
        for result in cursor.stored_results():
            queryResult = result.fetchall()

        #return queryResult
        for scriptInfo in queryResult:
            ScriptList.append( Script.Script(scriptInfo[0], scriptInfo[1], scriptInfo[2]) )

        return ScriptList

    def getInputFileRequirementListbyId(self, scriptId):
        return 1
    def getInputParmRequirementLIstbyId(self, scriptId):
        return 1
    def getInputFileDescription(self, scriptId, fileId):
        return 1
    def getInputParmDescription(self, scriptId, parmId):
        return 1


