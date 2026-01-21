#python program to follow a pattern.
rows = int(input("Please enter the number of rows: "))
for x in range(rows, 0, -1):
    for y in range(1, x+1):
        print(y, end=" ")
    print()