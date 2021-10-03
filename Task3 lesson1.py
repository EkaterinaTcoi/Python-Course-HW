#Task 3
#Write a program that allows user to enter their favourite starter, main course, dessert and drink.
#Concatenate these and output a message which says –“Your favourite meal is  .........with a glass of....”

start = input("Hi! What is your favourite starter?:")
main_dish = input("What is your favourite main dish?:")
course = input("Which course do you prefer?:")
dessert = input("What do you like eat on dessert?:")
drink = input("last one! Your favourite drink?:")


import random
myList = [start,main_dish, course, dessert]
x = random.choice(myList)

print("Your favourite meal is " + x + " with a glass of "+ drink)

