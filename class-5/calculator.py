import sys

def addition(num1, num2):
    add = num1 + num2
    return f"Value of the addition: {add}"

def subtraction(num1, num2):
    sub = num1 - num2
    return f"Value of the Subtraction: {sub}"

def multiplication(num1, num2):
    mul = num1 * num2
    return f"Value of the multiplication: {mul}"

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
   output = addition(num1, num2)

elif operation == "subtraction":
    output = subtraction(num1, num2)

elif operation == "multiplication":
    output = multiplication(num1, num2)    


print(output)


# Command line arguments are used to excute the program that what you have provided input values through cli

# python3 calculator.py 2 addition 3
# python3 calculator.py 10 subtraction 2
# python3 calculator.py 5 multiplication 2