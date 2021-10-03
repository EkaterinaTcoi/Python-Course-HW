#Task 3 Lesson 2
#Write a program which will ask for two numbers from a user. Then offer an option menu to the user giving them a choice of maths operators. Once the
#user has selected which operator they wish to use, perform the calculation by using a procedure and passing parameters

def function_1():
    num1 = input("Enter number 1:")
    num2 = input("Enter number 2:")
    opr = input("Enter\n\"a\" for +\n\"b\" for -\n\"c\" for /\n\"d\" for *")

    if opr == "a":
        print(float(num1) + float(num2))
    elif opr == "b":
        print(float(num1) - float(num2))
    elif opr == "c":
        print(float(num1) / float(num2))
    elif opr == "d":
        print(float(num1) * float(num2))
    else:
        print("Enter error!" )

    return opr

message = function_1()
print(message)
