#Created by Sam Stuyvenberg
#Conditional Statements

number = int(input("Enter a number: "))
if number > 0:
    print("I'ts Possitive.")
elif number > 1000:
    print("It's A large figure")
elif number > 1000000:
    print("It's A larger figure")
else:
    print("It's a negative number")
