class Task(object):
    TaskId = ''
    ScriptId = ''
    ScriptType = ''
    Parm = ''
    IsFinished = ''

    def __init__( self, _TaskId, _ScriptId, _ScriptType, _Parm ):
        self.TaskId = _TaskId
        self.ScriptId = _ScriptId
        self.ScriptType = _ScriptType
        self.Parm = _Parm
        return
    
