#Program to swap two numbers using a third variable.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Values of variables before swapping: x =", x, "y =", y)
temp = x
x = y
y = temp
print("Values of variables after swapping: x =", x, "y =", y)