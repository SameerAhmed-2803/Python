import random

def printMenu():
    print("1. Roll normal 6 side die")
    print("2. Roll a D20 die")
    print("Exit")

def dice_roll():
    num = random.randint(1,6)
    return print("Your random dice roll is",num)

def d20die():
    num = random.randint(1, 20)
    return print("Your D20 dice roll is",num)    

dice_roll()
d20die()