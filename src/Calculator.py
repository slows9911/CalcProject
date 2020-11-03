class Calculator:
    result = 0

def addition(d1, d2):
    return d1 + d2

def subtraction(d1, d2):
    return d1 - d2

def multiplication(d1, d2):
    return d1 * d2

def division(d1, d2):
    return d1 / d2

def squareNumber(d1):
    return d1 * d1

def squareRoot(d1):
    return d1**(1/2.0)

class calculator:

    result = 0

    def __init__(self):
        self.result = 1
        pass

    def add(self, d1, d2):
        self.result = addition(d1, d2)
        return self.result

    def sub(self, d1, d2):
        self.result = subtraction(d1, d2)
        return self.result

    def mult(self, d1, d2):
        self.result = multiplication(d1, d2)
        return self.result

    def div(self, d1, d2):
        self.result = division(d1, d2)
        self.result = float("{:.3f}".format(self.result))
        return self.result

    def sqr(self, d1):
        self.result = square(d1)
        return self.result

    def sqrt(self, d1):
        self.result = squareRoot(d1)
        self.result = float("{:.3f}".format(self.result))
        return self.result