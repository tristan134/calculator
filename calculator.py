import math

print("\n----------------------------")
print("Calculator MathPower III")
print("----------------------------")


elements = []
file = "calculator.txt"


def check(value):
    if value.startswith('-') and value[1:].isdigit():
        number = int(value)
        return number
    elif value.isdigit():
        number = int(value)
        return number
    else:
        return 0


def addition(number1, number2):
    add = number1 + number2
    print("Result=", add)
    elements.append(add)


def subtraction(number1, number2):
    sub = number1 - number2
    print("Result=", sub)
    elements.append(sub)


def multiplication(number1, number2):
    mul = number1 * number2
    print("Result=", mul)
    elements.append(mul)


def division(number1, number2):
    try:
        div = number1 / number2
        print("Result=", div)
        elements.append(div)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError as v:
        print("Invalid Value")
        return None
    except Exception as e:
        print("Operation Error:", e)
        return None


def firstbinomial(number1, number2):
    binomial1 = ((number1*number1)+(2*number1*number2)+(number2*number2))
    print("Result=", binomial1)
    elements.append(binomial1)


def secondbinomial(number1, number2):
    binomial2 = ((number1 * number1) - (2 * number1 * number2) + (number2 * number2))
    print("Result=", binomial2)
    elements.append(binomial2)


def thirdbinomial(number1, number2):
    binomial3 = ((number1 * number1) - (number2 * number2))
    print("Result=", binomial3)
    elements.append(binomial3)


def pqformula(number1, number2):
    try:
        pqpos = (number1 * (-1) / 2) + math.sqrt(((number1 / 2) * (number1 / 2)) - number2)
        pqneg = (number1 * (-1) / 2) - math.sqrt(((number1 / 2) * (number1 / 2)) - number2)
        print("Result(+)=", pqpos)
        print("Result(-)=", pqneg)
        elements.append(pqplus)
        elements.append(pqminus)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError:
        print("Invalid Value")
        return None
    except Exception as e:
        print("Operation Error:", e)
        return None


def abcformula(number1, number2, number3):
    try:
        abcpos = (((number2 * (-1)) + math.sqrt(number2 * number2 - 4 * number1 * number3)) / 2 * number1)
        abcneg = (((number2 * (-1)) - math.sqrt(number2 * number2 - 4 * number1 * number3)) / 2 * number1)
        print("Result(+)=", abcpos)
        print("Result(-)=", abcneg)
        elements.append(abcpos)
        elements.append(abcneg)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError:
        print("Invalid Value")
        return None
    except Exception as e:
        print("Operation Error:", e)
        return None


def operations():
    print("\n1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. Exit")
    choice = input("Menu: ")
    menuoperations = check(choice)
    if menuoperations > 5 or menuoperations < 1:
        print("Invalid option")
    elif menuoperations in {1, 2, 3, 4, 5}:
        print("\n")
        digit1 = input("First number: ")
        digit2 = input("Second number: ")
        num1 = check(digit1)
        num2 = check(digit2)
        print("\n")
        if menuoperations == 1:
            addition(num1, num2)
        elif menuoperations == 2:
            subtraction(num1, num2)
        elif menuoperations == 3:
            multiplication(num1, num2)
        elif menuoperations == 4:
            division(num1, num2)
        elif menuOperatoren == 5:
            print("Exit")


def formulas():
    print("\n1. Binomial formulas")
    print("2. Square formulas")
    print("3. Exit")
    choice = input("Menu: ")
    menuformulas = check(choice)
    if menuformulas > 3 or menuformulas < 1:
        print("Invalid option")
    elif menuformulas in {1, 2, 3}:
        if menuformulas == 1:
            print("")
            print("1. first binomial formula (a^2+2ab+b^2)")
            print("2. second binomial formula (a^2-2ab+b^2)")
            print("3. third binomial formula (a^2-b^2)")
            print("4. Exit")
            choice = input("Menu: ")
            menubinomials = check(choice)
            if menubinomials > 4 or menubinomials < 1:
                print("Invalid option")
            elif menubinomials in {1, 2, 3, 4}:
                print("")
                digit1 = input("First number: ")
                digit2 = input("Second number: ")
                num1 = check(digit1)
                num2 = check(digit2)
                print("\n")
                if menubinomials == 1:
                    firstbinomial(num1, num2)
                elif menubinomials == 2:
                    secondbinomial(num1, num2)
                elif menubinomials == 3:
                    thirdbinomial(num1, num2)
                elif menubinomials == 4:
                    print("Exit")
        elif menuformulas == 2:
            print("")
            print("1. pq-formula")
            print("2. abc-formula")
            print("3. Exit")
            choice = input("Menu: ")
            menusquare = check(choice)
            print("\n")
            if menusquare > 4 or menusquare < 1:
                print("Invalid option")
            elif menusquare in {1, 2, 3}:
                if menusquare == 1:
                    digit1 = input("First number: ")
                    digit2 = input("Second number: ")
                    p = check(digit1)
                    q = check(digit2)
                    pqformula(p, q)
                elif menusquare == 2:
                    digit1 = input("First number:")
                    digit2 = input("Second number:")
                    digit3 = input("Third number:")
                    a = check(digit1)
                    b = check(digit2)
                    c = check(digit3)
                    abcformula(a, b, c)
                elif menusquare == 3:
                    print("Exit")
        elif menuformulas == 3:
            print("Exit")


def miscellaneous():
    print("1. Save results in textfile")
    print("2. Read results from textfile")
    choice = input("Menu: ")
    menumiscellaneous = check(choice)
    if menumiscellaneous > 2 or menumiscellaneous < 1:
        print("Invalid option")
    elif menumiscellaneous in {1, 2}:
        if menumiscellaneous == 1:
            write_list(listElemente)
        elif menumiscellaneous == 2:
            print(read_list())


def write_list(resultlist):
    try:
        print("Started writing list data into a txt file")
        with open(file, "a") as wfile:
            wfile.write(str(resultlist) + "\n")
            print("All results are saved in calculator.txt")
            print("The list will be cleared")
            del listElemente[:]
    except FileNotFoundError:
        print("File could not be found")
    except Exception as e:
        print("An error occurred while writing", e)
        return None


def read_list():
    try:
        with open(file, 'r') as rfile:
            readfile = rfile.readlines()
            return readfile
    except FileNotFoundError:
        print("File could not be found")
        return None
    except Exception as e:
        print("An error occurred while reading", e)
        return None


while True:
    print("")
    print("1. Basic arithmetic operations")
    print("2. Formulas")
    print("3. Miscellaneous")
    print("4. Exit")
    choice = input("Menu: ")
    menu = check(choice)
    if menu > 4 or menu < 1:
        print("Invalid option")
    elif menu in {1, 2, 3, 4}:
        if menu == 1:
            operations()
        elif menu == 2:
            formulas()
        elif menu == 3:
            miscellaneous()
        elif menu == 4:
            break

print("\nBye.")
