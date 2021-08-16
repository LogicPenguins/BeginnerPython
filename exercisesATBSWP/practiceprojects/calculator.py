# Program does not currently work because the module calculator was from my old PyCharm projects page and since
# I moved to Visual Studio Code, it's no longer here. I'm too lazy to remake a calculator module and class
# But I'm keeping this project in here for memories because it was the first project I made on my own.

import calculator

types = input("""
Operation Options:
Addition - Adds two values
Subtraction - Subtracts first value from second value
Multiplication - Multiplies two values
Division - Divides first value from second value
Square - Finds the square of a value
Operation: 
""").lower()
if types == "addition":
    try:
        x = int(input("First Number: "))
        y = int(input("Second Number: "))
        result = calculator.Addition(x, y)
        print(result.add())
    except:
        print("That is not a number.")
elif types == "subtraction":
    try:
        x = int(input("First Number: "))
        y = int(input("Second Number: "))
        result = calculator.Subtraction(x, y)
        print(result.subtract())
    except:
        print("That is not a number.")
elif types == "multiplication" or types == "multiply":
    try:
        x = int(input("First Number: "))
        y = int(input("Second Number: "))
        result = calculator.Multiplication(x, y)
        print(result.multiply())
    except:
        print("That is not a number.")
elif types == "division":
    try:
        x = int(input("First Number: "))
        y = int(input("Second Number: "))
        result = calculator.Divide(x, y)
        print(result.divide())
    except:
        print("That is not a number. ")
elif types == "square":
    try:
        x = int(input("Number: "))
        result = calculator.Square(x)
        print(result.square())
    except:
        print("That is not a number.")
else:
    print("That is not an operation. ")
