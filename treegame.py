import random
name = input("What is your name? ")
print("Welcome to the tree game ", name, "!")
print("Rules: A random number will be given to you. You will need to complete the tree in order to win! Good Luck!")
number = random.randint(1,300)
print(" The number given for the tree is: ", number) 
number1 = int(input("Give me number 1 for the left side of the tree: "))
print(name," has chosen ", number1)
if number1 < number:
    print("Good choice!")
else:
    print("No!")
number2 = int(input("Give me number 2 for the right side of number 1: "))
print(name," has chosen ", number2)
if number2 > number1 and number2 < number:
    print("Correct!")
else:
    print("No!")
number3 = int(input("Give me number 3 for the left side of number 1: "))
print(name," has chosen ", number3)
if number3 < number1: 
    print("Wowza!")
else:
    print("No!")
a = input("Shall we move onto the right side of the tree? ")
if a == 'yes':
    number4 = int(input("Fantastic! Give me number 4 for the right side of the tree: "))
    print(name," has chosen ", number4)
    if number4 > number:
            print("Bravo!")
    else:
            print("No!")
    number5 = int(input("Give me number five for the right side of number 4: "))
    print(name," has chosen ", number5)
    if number5 > number4:
            print("Bravo")
    else:
            print("No!")
    number6 = int(input("Last Number! Give me number six for the left side of number 4: "))
    print(name," has chosen ", number6)
    if number6 < number4 and number6 > number:
            print("Good Work! ")
    else:
            print("No!")
print(" Your tree looks like this:")
print("             ", number)
print("  ", number1,"                ", number4)
print( number3, "   ", number2,"        ", number6,"   ", number5)
    