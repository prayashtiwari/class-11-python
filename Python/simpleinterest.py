#reading principal amount, rate and time.
principal = float(input("enter amount:"))
time = float(input("enter time in years: "))
rate = float(input("enter rate of interest: "))
simpleinterest = (principal * rate * time) / 100
print("The simple interest is:", simpleinterest)