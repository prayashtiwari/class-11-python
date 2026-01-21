#program to input the multiplier and the multiplicand and display the multiplication table.
num1 = int(input("Enter the multiplier: "))
num2 = int(input("Enter the multiplicand: "))
while num2 <= 10:
    result = num1 * num2
    print(num1, "x", num2, "=", result)
    num2 += 1
# End of the program