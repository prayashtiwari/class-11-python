#program to detect the smallest and the largest number given by the user.
smallest = 0
largest = 0

for a in range(0, 5):
    x = int(input("Please enter a number: \n"))
    if(a==0):
        smallest = largest = 0
    if(x<smallest):
        smallest = x
    if(x>largest):
        largest = x
print("The smallest number is:", smallest)
print("The largest number is: ", largest)
