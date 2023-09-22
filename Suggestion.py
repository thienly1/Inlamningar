class Suggestion:
    
    def __init__(self, order, content):
        self.order = order
        self.content = content
    def toString(self):
        print(self.order, ": ", self.content) 
        