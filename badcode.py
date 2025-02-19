def addition_function(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    elif type(a) == float and type(b) == float:
        return a + b
    elif type(a) == int and type(b) == float:
        return a + b
    elif type(a) == float and type(b) == int:
        return a + b
    else:
        return "Invalid Input"

class Calculator:
    def init(self):
        pass

    def s(self, a, b):
        if type(a) == int and type(b) == int:
            return a - b
        elif type(a) == float and type(b) == float:
            return a - b
        elif type(a) == int and type(b) == float:
            return a - b
        elif type(a) == float and type(b) == int:
            return a - b
        else:
            return 0

class multiplyy(Calculator):
    def multiply(self, a, b):
        if type(a) == int and type(b) == int:
            return a * b
        elif type(a) == float and type(b) == float:
            return a * b
        elif type(a) == int and type(b) == float:
            return a * b
        elif type(a) == float and type(b) == int:
            return a * b
        else:
            return "Invalid Input"