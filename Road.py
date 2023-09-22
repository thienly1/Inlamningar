class Road:
    def __init__(self, name):
        self.name = name
        self.tools = []
        self.suggestions = []
    def addTools(self, tool):
        self.tools.append(tool)
    def addSuggestions(self, suggestion):
        self.suggestions.append(suggestion)
    def getTools(self):
        return self.tools
    def getSuggestions(self):
        return self.suggestions      
    def toString(self):
        pass
