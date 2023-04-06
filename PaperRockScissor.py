#Issa
import random

player = input("Enter rock, paper or scissor: ")

#paper = "0"
#rock = "1"
#scissor = "2"

#RandomNum = random.randint(0,2)

RandomNum = random.choice(["rock", "paper", "scissor"])
player = player.lower()

if player == "scissor" and RandomNum == "paper":
    print("You won")
elif player == "scissor" and RandomNum == "rock":
    print("The computer won")
elif player == "scissor" and not(RandomNum == "paper" or RandomNum == "rock"):
    print("Tight")
            
elif player == "rock" and RandomNum == "scissor":
    print("You won")
elif player == "rock" and RandomNum == "paper":
    print("The computer won")
elif player == "rock" and not(RandomNum == "paper" or RandomNum == "scissor"):
    print("Tight")
            
elif player == "paper" and RandomNum == "rock":
    print("You won")
elif player == "paper" and RandomNum == "scissor":
    print("The computer won")
elif player == "paper" and not(RandomNum == "rock" or RandomNum == "scissor"):
    print("Tight")
    
else:
    print("No winner! Please enter the correct input")
