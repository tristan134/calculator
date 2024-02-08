import math

print("\n----------------------------")
print("Calculator MathPower III")
print("----------------------------")


listElemente = []
file = "calculator.txt"


def probe(value):
    if value.startswith('-') and value[1:].isdigit():
        number = int(value)
        return number
    elif value.isdigit():
        number = int(value)
        return number
    else:
        return 0


def addition(number1, number2):
    plus = number1 + number2
    print("Result=", plus)
    listElemente.append(plus)


def subtraction(number1, number2):
    minus = number1 - number2
    print("Result=", minus)
    listElemente.append(minus)


def multiplication(number1, number2):
    mal = number1 * number2
    print("Result=", mal)
    listElemente.append(mal)


def division(number1, number2):
    try:
        geteilt = number1 / number2
        print("Result=", geteilt)
        listElemente.append(geteilt)
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
    listElemente.append(binomial1)


def secondbinomial(number1, number2):
    binomial2 = ((number1 * number1) - (2 * number1 * number2) + (number2 * number2))
    print("Result=", binomial2)
    listElemente.append(binomial2)


def thirdbinomial(number1, number2):
    binomial3 = ((number1 * number1) - (number2 * number2))
    print("Result=", binomial3)
    listElemente.append(binomial3)


def pqformula(number1, number2):
    try:
        pqplus = (number1 * (-1) / 2) + math.sqrt(((number1 / 2) * (number1 / 2)) - number2)
        pqminus = (number1 * (-1) / 2) - math.sqrt(((number1 / 2) * (number1 / 2)) - number2)
        print("Result(+)=", pqplus)
        print("Result(-)=", pqminus)
        listElemente.append(pqplus)
        listElemente.append(pqminus)
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
        abcplus = (((number2 * (-1)) + math.sqrt(number2 * number2 - 4 * number1 * number3)) / 2 * number1)
        abcminus = (((number2 * (-1)) - math.sqrt(number2 * number2 - 4 * number1 * number3)) / 2 * number1)
        print("Result(+)=", abcplus)
        print("Result(-)=", abcminus)
        listElemente.append(abcplus)
        listElemente.append(abcminus)
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
    menuoperations = probe(choice)
    if menuoperations > 5 or menuoperations < 1:
        print("Invalid option")
    elif menuoperations in {1, 2, 3, 4, 5}:
        print("\n")
        digit1 = input("First number: ")
        digit2 = input("Second number: ")
        zahl1 = probe(digit1)
        zahl2 = probe(digit2)
        print("\n")
        if menuoperations == 1:
            addition(zahl1, zahl2)
        elif menuoperations == 2:
            subtraction(zahl1, zahl2)
        elif menuoperations == 3:
            multiplication(zahl1, zahl2)
        elif menuoperations == 4:
            division(zahl1, zahl2)
        elif menuOperatoren == 5:
            print("Exit")


def formulas():
    print("\n1. Binomial formulas")
    print("2. Square formulas")
    print("3. Exit")
    choice = input("Menu: ")
    menuformulas = probe(choice)
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
            menubinomials = probe(choice)
            if menubinomials > 4 or menubinomials < 1:
                print("Invalid option")
            elif menubinomials in {1, 2, 3, 4}:
                print("")
                digit1 = input("First number: ")
                digit2 = input("Second number: ")
                zahl1 = probe(digit1)
                zahl2 = probe(digit2)
                print("\n")
                if menubinomials == 1:
                    firstbinomial(zahl1, zahl2)
                elif menubinomials == 2:
                    secondbinomial(zahl1, zahl2)
                elif menubinomials == 3:
                    thirdbinomial(zahl1, zahl2)
                elif menubinomials == 4:
                    print("Exit")
        elif menuformulas == 2:
            print("")
            print("1. pq-formula")
            print("2. abc-formula")
            print("3. Exit")
            choice = input("Menu: ")
            menusquare = probe(choice)
            print("\n")
            if menusquare > 4 or menusquare < 1:
                print("Invalid option")
            elif menusquare in {1, 2, 3}:
                if menusquare == 1:
                    digit1 = input("First number: ")
                    digit2 = input("Second number: ")
                    p = probe(digit1)
                    q = probe(digit2)
                    pqformula(p, q)
                elif menusquare == 2:
                    digit1 = input("First number:")
                    digit2 = input("Second number:")
                    digit3 = input("Third number:")
                    a = probe(digit1)
                    b = probe(digit2)
                    c = probe(digit3)
                    abcformula(a, b, c)
                elif menusquare == 3:
                    print("Exit")
        elif menuformulas == 3:
            print("Exit")


def miscellaneous():
    print("1. Save results in textfile")
    print("2. Read results from textfile")
    choice = input("Menu: ")
    menumiscellaneous = probe(choice)
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
    menu = probe(choice)
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
