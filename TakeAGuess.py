#Issa
#11/7/22

import random  

again = "yes"  
while again == "yes":
    num = random.randint(0,20)
    
    guess = int(input("Enter guess: "))

    while num != guess:
        if guess < 3:
            print("Congrats! Keep trying")
        if num < guess:
            print("Incorrect")
            print("Your guess is too high, go lower")
        if num > guess:
            print("Incorrect")
            print("Your guess is too low, go high")
        
        guess = int(input("Enter guess: "))
 
    print("Congrats!  You got it correct!")
    again = input("Enter yes to go again or No to quit: ")
    again = again.lower()  
