# calculator.py

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Division by zero not allowed"
        return self.a / self.b

    def average(self):
        return (self.a + self.b) / 2
