def add(num1, num2): #function takes in two numbers as parameters and adds them together, returning the sum
    return num1 + num2

def subtract(num1, num2): #function takes in two numbers as parameters and subtracts them, returning the difference
    return num1 - num2 

def multiply(num1, num2): #function takes in two numbers as parameters and multiplies them together, returning the product
    return num1 * num2

def main():
    choice = 0 #initialize user choice variable
    while(choice != 10):
        choice = int(input('Enter your option for the calculator. (1. Add, 2. Subtract, 3. Multiply, 10. Quit)')) #ask user to input choice, looping indefinitely until user inputs 10
        if(choice == 1):
            num1 = int(input("Enter your first number"))
            num2 = int(input("Enter your second number"))
            print('Result: ', add(num1, num2)) #if choice 1, add two numbers and print result
        elif(choice == 2):
            num1 = int(input("Enter your first number"))
            num2 = int(input("Enter your second number"))
            print('Result: ', subtract(num1, num2)) #if choice 2, subtract two numbers and print result
        elif(choice == 3):
            num1 = int(input("Enter your first number"))
            num2 = int(input("Enter your second number"))
            print('Result: ', multiply(num1, num2)) #if choice 3, multiply two numbers and print result
        elif(choice == 10):
            break #if choice 10, exit while loop
        else:
            print("Invalid option. Please choose 1, 2, 3, or 10.") #if choice not 1, 2, 3, or 10, invalid choice, loop back to choice input

if __name__ == '__main__':
    main()        #run main function