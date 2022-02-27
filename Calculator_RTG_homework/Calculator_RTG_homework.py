
import math

while True:
    operator = input("\n1 Addition \n2 Subtraction \n3 Multiplication \n4 Devision \n5 Squer \n6 Sqr root \n\nQ/q to Exit \n\n :")

    if operator == 'q'  or operator == 'Q':
        break

    if operator == "1":
        while True:
            try:
                x = float(input("Number 1 : "))
                y = float(input("Number 2 : "))
            except ValueError:
                print("Please enter a number")
            else:
                 print(x, "+", y, "=", x + y)
                 break  
            
    elif operator == "2":
        while True:
            try:
                x = float(input("Number 1 : "))
                y = float(input("Number 2 : "))
            except ValueError:
                print("Please enter a number")
            else:
                print(x, "-", y, "=", x - y)
                break

    elif operator == "3":

        while True:
            try:
                x = float(input("Number 1 : "))
                y = float(input("Number 2 : "))
            except ValueError:
                print("Please enter a number")
            else:
                print(x, "*", y, "=", x * y)
                break

    elif operator == "4":

        while True:
            try:
                x = float(input("Number 1 : "))
                y = float(input("Number 2 : "))
            except ValueError:
                print("Please enter a number")
            else:
                if y != 0:
                    print(x, "/", y, "=", x / y)
                    break
                else:
                    print("cannot devide by zero!")

    elif operator == "5":

         while True:
            try:
                x = float(input("Number 1 : "))
            except ValueError:
                print("Please enter a number")
            else:
                print(x, "squred =", math.pow(x, 2))
                break

    elif operator == "6":

         while True:
            try:
                x = float(input("Number 1 : "))
            except ValueError:
                print("Please enter a number")
            else:        
                if x > 0:
                    print("Square root of", x, "is", math.sqrt(x))
                    break
                else:
                    print("Must be a positve integer \n")

    else:
        print("Can't do that, pls try again")