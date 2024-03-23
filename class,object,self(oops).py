class F15:
    def light(self):
        print("switching on ")
    def fan(self,speed):
        print("fan is on is 5")
        self.s=speed
    def cpu(self):
        print("powering on")
        print(self.s)
chandu=F15()
chandu.light()
chandu.fan(2)                
chandu.cpu()