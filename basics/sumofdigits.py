#program to determine the sum of the digits in a given number.
sum = 0
n = int(input("Enter a number:\n"))
while n>0:
    digit = n%10
    sum = sum+digit
    n = n//10
print("The sum of the digits in the number are:", sum)