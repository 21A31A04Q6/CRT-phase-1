class prag:
    def place(self):
        print("Surampalem")
class dept(prag):
    def branch(self,branch):
        print("the branch is:",branch)
p=dept()
p.place()
p.branch("ece")        
class year(prag):
    def c(self,clg):
        print("the year is:",clg)
o=year()
o.c("third")
o.place()        
