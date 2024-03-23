class prag:
    def place(self):
        print("Surampalem")
    def branch(self,branch):
        print("the branch is:",branch)    
class pragati(prag):
    def place(self):
        print("kakinada")
obj=pragati()
obj.place()
obj.branch("ece")                