"""
- generate a random number 1- 20 
- ask the user for their name 
- tell the user that they have to guess a number 1-20
- they only have 6 trys.
- high or low 
- if equals tell them how many trys it took
- if never, tell them the number.
"""
import random
import sys
magic_number = random.randint(1, 20)

print("Hello there! what is your name?")
name = input()
print("welcome", name, ". let's play a game. I know a magic number, try to guess it. I will give you a hint, it's between 1 and 20. be careful you only have 6 trys")

for trys in range(1, 7):
    try:
        guess = int(input())
    except ValueError:
        print("opps, there's an error")
        sys.exit()

    if guess > magic_number:
        print("oh no, that, too much")
    elif guess < magic_number:
        print("no. that's too little.")
    else:
        print("that is true! congrats. it took you", trys, "tries to guess")
        break

if guess != magic_number:
    print("oh no, you ran out of trys. my magic number was", magic_number)
