#Task 2
#Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number. You should use a minimum of 3 jokes

try:

    number = int(input("What is your favourite number between 1 and 100"))

    if number < 1 or number > 100:
        print("The number must be between 1 and 100")
    elif number <= 30:
         print("You knew that most people choose a number between 1 and 30. You're hardly original, but you're a great team player!")
    elif number >=60:
         print("You sure are an original fruit! Some kind of a Dragon fruit or Papaya!")
    elif 60 >= number >= 30:
         print("My developer didin't have the wit or sense of humour to come up with a joke on that number :/ Count youeself lucky. You got off easy!")
    else:
        print("Error! Try one more time!")
except:
    print("Something went wrong! Try one more time!")


