class MinStack :
    def __init__(self):
        self.ana_stack=[]
        self.min_stack=[]
    
    def push(self,data):
        self.ana_stack.append(data)
        if len(self.min_stack)==0 :
             self.min_stack.append(data)
        else:
            if self.min_stack[-1]>=data:
                 self.min_stack.append(data)
            else:
                return
    
    def pop(self):
        a=self.ana_stack[-1]
        self.ana_stack.pop()
        if a == self.min_stack[-1]:
            return self.min_stack.pop()
        else:
            return
    
    def top(self):
        return self.ana_stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
    
        