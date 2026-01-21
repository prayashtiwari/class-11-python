#program to greet user based on their gender (Male or Female), using functions
gender = input("Please enter your gender: \n")
name = input("Please enter your name: \n")
def prefix(name, gender):
    if(gender == "M" or gender == "Male"):
        print("Hello, Mr.", name)
    elif(gender == "F" or gender == "Female"):
        print("Hello Ms.", name)
    else:
        print("Please use a valid letter/word to denote your gender.")
prefix(name, gender)