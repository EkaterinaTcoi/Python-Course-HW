#Task 1
#Write a program that does the following:
#a) Stores a random number (1-10) in a variable –see hint below.
#b) Asks a user for their name and stores this in a variable.
#c) Asks a user to guess the number between 1 and 10.
#d) Tells the user whether they have guessed correctly

import random

x = random.randint(1,10)

name = input("What is your name?")
number = int(input("Chose a number from 1 to 10"))

if x == number:
    print("Hi "+ name +" you have chose the right number!" )
else:
    print("Hi "+ name +" you have chose the wrong number! I chose number "+ str(x))


