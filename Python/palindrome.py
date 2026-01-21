#program to find out the palindrome of a number and mention if its non-existent.
n = int(input("Enter a number:"))
temp = n
reverse = 0
while(n>0):
    digit = n%10
    reverse = reverse*10 + digit
    n = n//10
if(temp == reverse):
    print("Palindrome")
else:
    print("Not a palindrome")