#Issa
#9/29/22

import random

number1 = random.randint(0,100)
number2 = random.randint(0,100)

print(number1,number2, sep = " ")
print("Substract the first number by the second")

Answer = int(input("Guess the answer: "))

if number1-number2 == Answer:
 print("You are correct! The answer is: ",number1-number2)

else:
 print("You are not correct! The correct answer is: ",number1 - number2)
             
