from random import *

print("Hello, what's your name?")
print()

name = input("My name is ")
print()

print("well, " + name + " i'm thinking of a number between 1 to 20\ntake a guess..!")
print()

rnd_number = randint(1, 20)

Guesses_no = 0

try:
    while Guesses_no < 3:
        guess = input("Gussed number is :- ")

        if int(guess) > rnd_number:
            print("number is too high")
            print("Try again..!")
            # Guesses_no = Guesses_no + 1
            print()

        elif int(guess) < rnd_number:
            print("Number is too low")
            print("Try again..!")
            
            print()

        else:
            print()
            print("Good job! you've guessed in " + str(Guesses_no) + " try..!")
            print("That number is " + str(rnd_number))
            break

        Guesses_no = Guesses_no + 1

        if Guesses_no == 3:
            raise Exception()

except:
    print("That number was " + str(rnd_number))
    print("You've lost..!")