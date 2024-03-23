class F15:
    def light(self):
        print("switching on ")
class shopping(F15):
    def size(self,size): 
        self.s=size
    def display(self):
        print("the details of user are:")
        print(self.d,self.p,self.s)
class study(shopping):
    def s1(self,standard):
        print("the required standard is:",standard)
        self.st=standard
    def s2(self):
        print("graduated")
a=study()
a.size(22)
a.light()
a.s1(12)
a.s2()                    