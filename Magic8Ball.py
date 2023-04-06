#Issa
#9/29/22

import random

#Problem 5: Magic 8 Ball
#A popular children’s toy is the magic 8 ball. You ask this toy a question and you flip it over and it
#provides an answer. You will recreate this program using the random number generator and the if
#statement. You should have a minimum of 5 statements.
#You do not need to do anything with the original question.

question = str(input("Please ask a question: "))

x = random.randint(0,8)

if x == 1:

    print("Without A Doubt!")

elif x == 2:

    print("Better Not Tell You Now!")

elif x == 3:

    print("Unsure!")
elif x == 4:
    print("Signs Point To Yes!")

elif x == 5:

    print("You are correct!")

elif x == 6:

    print("Yes Definitely!")

elif x == 7:

    print("Don't Count On It!")

else:
    print("Try Again!")
