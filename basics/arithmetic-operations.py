#python program to input two numbers and perform basic arithmetic operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#the following is an improvisation to handle division/modulus by zero
if num2 == 0:
    print("Warning: Division and Modulus by zero is not allowed.")
print("Printing the results of arithmetic operations:")
print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1 / num2)
print("Modulus: ", num1 % num2)