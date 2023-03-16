from random import *
secnum = randint(1,50)
print("Hey.. I'm thinking of a Number between 1 and 50")
print("Try to Guess it in 5 Chances")
chances = 0
for i in range(5):
    chances += 1
    guess = int(input("Your Guess:"))
    if guess<secnum:
        print("Your Guess is Low")
    elif guess>secnum:
        print("Your Guess is High")
    else:
        break
if guess==secnum:
    print("Congratulations... :-)")
    print("You have guessed the Number in {} chances".format(chances))
else:
    print("Better Luck Next Time")
    print("Secret Number is",secnum)
