#Issa
#9/29/2022

import random

RandomNum = int(input("Please enter 0 for heads or 1 for Tails: "))
number = random.randint(0,1)

if number == RandomNum:                 
    print("You are correct!")
    
else:
    print("You are not correct. Please try again!")
