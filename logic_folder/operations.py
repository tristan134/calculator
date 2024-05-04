import dependencies


def operations():
    print("\n1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. Exit")
    choice = input("Menu: ")
    menuoperations = dependencies.check(choice)
    if menuoperations > 5 or menuoperations < 1:
        print("Invalid option")
    elif menuoperations in {1, 2, 3, 4, 5}:
        print("\n")
        digit1 = input("First number: ")
        digit2 = input("Second number: ")
        num1 = dependencies.check(digit1)
        num2 = dependencies.check(digit2)
        print("\n")
        if menuoperations == 1:
            addition(num1, num2)
        elif menuoperations == 2:
            subtraction(num1, num2)
        elif menuoperations == 3:
            multiplication(num1, num2)
        elif menuoperations == 4:
            division(num1, num2)
        elif menuoperations == 5:
            print("Exit")


def addition(number1, number2):
    add = number1 + number2
    print("Result=", add)
    dependencies.elements.append(add)


def subtraction(number1, number2):
    sub = number1 - number2
    print("Result=", sub)
    dependencies.elements.append(sub)


def multiplication(number1, number2):
    mul = number1 * number2
    print("Result=", mul)
    dependencies.elements.append(mul)


def division(number1, number2):
    try:
        div = number1 / number2
        print("Result=", div)
        dependencies.elements.append(div)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError as v:
        print("Invalid Value")
        return None
    except Exception as e:
        print("Operation Error:", e)
        return None
