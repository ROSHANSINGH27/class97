import random
number=random.randint(1,9)
print("Number guessing game")
print("Guess a number between 1 to 9:-")
guess=input("enter your guess")
print(guess)

if(guess!=number):
     print("your guess was wrong")
     if(guess!=number):print("your guess was wrong")

if (guess==number):print("you won")

    

