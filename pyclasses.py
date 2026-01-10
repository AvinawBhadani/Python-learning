class Test:
    c = 10 # class variable or static variable
    def __init__(self, a, b): # Constructor
        self.a = a #Instance Variable
        self.b = b # Instance Variable

    def add(self): #Intance method
        print(Test.c) # Static variable always gets called using class name
        return self.a + self.b

    def sub(self): # Intance method
        return self.a - self.b
    
    @staticmethod
    def static(): # Static Method
        print("static")
    
    def calculate(price, tax_percentage):
        return price * tax_percentage / 100
    


t1 = Test(6,2)
print(t1)
t2 = Test(5,3)
print(t1.add())
print(t2.sub())
print(Test.calculate(100, 10))