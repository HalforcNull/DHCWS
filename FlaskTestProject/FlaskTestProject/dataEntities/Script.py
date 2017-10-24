
class Script:
    Name = ''
    Id =''
    Description = ''
    Type = ''
    IsOpenSource = False
    inputList = []
    outputList = []

    def __init__(self, Id, name, description):
        self.Id = Id
        self.Name = name
        self.Description = description
