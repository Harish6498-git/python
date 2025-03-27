import sys

def addition(num1, num2):
    add = num1 + num2
    return f"Value of the addition: {add}"

def subtraction(num1, num2):
    sub = num1 - num2
    return f"Value of the subtraction: {sub}"

def multiplication(num1, num2):
    mul = num1 * num2
    return f"Value of the multiplication: {mul}"

def division(num1, num2):
    div = num1 / num2
    return f"Value of the division: {div}"

def floor(num1, num2):
    floor = num1 // num2
    return f"Value of the floor: {floor}"

def modulus(num1, num2):
    mod = num1 % num2
    return f"Value of the modulus: {mod}"

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
    output = addition(num1, num2)

elif operation == "subtraction":
    output = subtraction(num1, num2)

elif operation == "multiplication":
    output = multiplication(num1, num2)

elif operation == "division":
    output = division(num1, num2)

elif operation == "floor":
    output = floor(num1, num2)

elif operation == "modulus":
    output = modulus(num1, num2)

print(output)
                    
