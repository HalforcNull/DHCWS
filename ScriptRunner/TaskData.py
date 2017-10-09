from enum import Enum
class TaskType(Enum):
    RScript = 1
    RMarkDown = 2
    Unknown = 0


class TaskData:
    TaskId = ''
    ScriptId = ''
    ScriptFile = ''
    TaskType = 0
