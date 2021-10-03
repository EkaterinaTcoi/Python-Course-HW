# Task 2 lesson 3
# Write a program to ask a student for their percentage mark and convert this to a grade.
# The conversion will be done in a function called mark_grade

def mark_grade():
    score = input("Enter your score:")

    if int(score) >= 86:
        output = "Congratulations, you have a high score: " + str(score)
    elif 86 >= int(score) >= 54:
        output = "Well done, you have a passing score: " + str(score)
    elif 1 > int(score) > 100:
        output = "Error! Incorrect input!"
    else:
        output = "Unfortunately, your score didn't pass. Don't give up! Keep going!: " + str(score)
    return output


text = mark_grade()
print(text)
