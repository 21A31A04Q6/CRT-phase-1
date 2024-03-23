class prag:
    def place(self):
        print("Surampalem")
class dept:
    def branch(self,branch):
        print("the branch is:",branch)
class year(prag,dept):
    def c(self,clg):
        print("the year is:",clg)
o=year()
o.place()
o.branch("ece")  
o.c("third")                                
