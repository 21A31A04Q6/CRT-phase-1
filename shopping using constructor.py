class shopping:
    def __init__(self,place):
        self.place=place
        print("welcome to ",place)
    def d_type(self,dress):
        self.d=dress
    def price(self,price):
        self.p=price
    def size(self,size): 
        self.s=size
    def display(self):
        print("the details of user are:")
        print(self.d,self.p,self.s,self.place)
radha=shopping("zudio")
radha.d_type("lehenga")
radha.price(3000) 
radha.size("xl")
radha.display()                   
