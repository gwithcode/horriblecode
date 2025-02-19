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

def main():
    print("Calculator")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    op = input("Enter operation (+, -, ): ")

    if op == '+':
        print("Result:", addition_function(int(a), int(b)))
    elif op == '-':
        calc = Calculator()
        print("Result:", calc.s(int(a), int(b)))
    elif op == '':
        adv_calc = multiplyy()
        print("Result:", adv_calc.multiply(int(a), int(b)))
    else:
        print("WRONGGGG IDIOT")

main()