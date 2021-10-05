#Task1 Lesson3
#Write a program that allows you to enter 4 numbers
#and stores them in a file called “Numbers”
#•3
#•45
#•83
#•21
#Have a go at ‘w’ ‘r’  ‘a’

from typing import Text

x = input("Enter number: 3, 45,83,21")
my_num: Text = open("Number.txt", "a")

my_num.write(x)

my_num.close()
