
while True:
    operator = input("1 Addition \n2 Subtraction \n3 Multiplication \n4 Devision \n5 Rasing power \n\nQ/q to Exit \n\n :")

    if operator == 'q'  or operator == 'Q':
        break

    x = float(input("Number 1 : "))
    y = float(input("Number 2 : "))

    if operator == "1":
        print('{} + {} = '.format(x, y))
        print(x + y)
    elif operator == "2":
        print(x - y)
    elif operator == "3":
        print(x * y)
    elif operator == "4":
        if y != 0:
            print(x / y)
        else:
            print("cannot devide by zero!")
    elif operator == "5":
        print(x**y)
    else:
        print("Can't do that, pls try again")
