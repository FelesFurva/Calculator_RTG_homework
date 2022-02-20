
import math

while True:
    operator = input("1 Addition \n2 Subtraction \n3 Multiplication \n4 Devision \n5 Rasing power \n6 Sqr root \n\nQ/q to Exit \n\n :")

    if operator == 'q'  or operator == 'Q':
        break

    if operator == "1":

        x = float(input("Number 1 : "))
        y = float(input("Number 2 : "))

        print('{} + {} = '.format(x, y))
        print(x + y)

    elif operator == "2":

        x = float(input("Number 1 : "))
        y = float(input("Number 2 : "))
        print(x - y)

    elif operator == "3":

        x = float(input("Number 1 : "))
        y = float(input("Number 2 : "))
        print(x * y)

    elif operator == "4":

        x = float(input("Number 1 : "))
        y = float(input("Number 2 : "))
        if y != 0:
            print(x / y)
        else:
            print("cannot devide by zero!")

    elif operator == "5":

        x = float(input("Number: "))
        print(x**2)

    elif operator == "6":

        x = float(input("Number: "))
        print(math.sqrt(x))

    else:
        print("Can't do that, pls try again")