from random import *

print("Hello, what's your name?")
print()

name = input("My name is ")
print()

print("well, " + name + " i'm thinking of a number between 1 to 20\ntake a guess..!")
print()

rnd_number = randint(1, 20)

Guesses_no = 0

print("You have only 3 tries...!")
print()

try:
    while Guesses_no < 3:
        guess = input("Gussed number is :- ")

        if guess.isdigit():

            Guesses_no = Guesses_no + 1

            if int(guess) > rnd_number:
                print("number is too high")
                print("Try again..!")
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

            if Guesses_no == 3:
                raise Exception()
            
        else:
            print("Please enter a valid digits..!\n")

except:
    print("The number was " + str(rnd_number))
    print("Oops! you lost..!")
