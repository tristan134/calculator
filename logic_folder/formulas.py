import dependencies
import math

cancel = False


def firstbinomial(number1, number2):
    binomial1 = ((number1 * number1) + (2 * number1 * number2) + (number2 * number2))
    print("Result=", binomial1)
    dependencies.elements.append(binomial1)


def secondbinomial(number1, number2):
    binomial2 = ((number1 * number1) - (2 * number1 * number2) + (number2 * number2))
    print("Result=", binomial2)
    dependencies.elements.append(binomial2)


def thirdbinomial(number1, number2):
    binomial3 = ((number1 * number1) - (number2 * number2))
    print("Result=", binomial3)
    dependencies.elements.append(binomial3)


def pqformula(number1, number2):
    try:
        pqpos = (number1 * (-1) / 2) + math.sqrt(((number1 / 2) * (number1 / 2)) - number2)
        pqneg = (number1 * (-1) / 2) - math.sqrt(((number1 / 2) * (number1 / 2)) - number2)
        print("Result(+)=", pqpos)
        print("Result(-)=", pqneg)
        dependencies.elements.append(pqpos)
        dependencies.elements.append(pqneg)
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
        dependencies.elements.append(abcpos)
        dependencies.elements.append(abcneg)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError:
        print("Invalid Value")
        return None
    except Exception as e:
        print("Operation Error:", e)
        return None


def binomial():
    global cancel
    while not cancel:
        print("\n1. first binomial formula (a^2+2ab+b^2)")
        print("2. second binomial formula (a^2-2ab+b^2)")
        print("3. third binomial formula (a^2-b^2)")
        print("4. Exit")
        choice = input("Menu: ")
        if choice == "4":
            break
        digit1 = input("First number: ")
        digit2 = input("Second number: ")
        num1 = dependencies.check(digit1)
        num2 = dependencies.check(digit2)
        match choice:
            case "1":
                firstbinomial(num1, num2)
            case "2":
                secondbinomial(num1, num2)
            case "3":
                thirdbinomial(num1, num2)
            case "4":
                cancel = True


def squareform():
    global cancel
    while not cancel:
        print("\n1. pq-formula")
        print("2. abc-formula")
        print("3. Exit")
        choice = input("Menu: ")
        if choice == "3":
            break
        match choice:
            case "1":
                digit1 = input("First number: ")
                digit2 = input("Second number: ")
                p = dependencies.check(digit1)
                q = dependencies.check(digit2)
                pqformula(p, q)
            case "2":
                digit1 = input("First number:")
                digit2 = input("Second number:")
                digit3 = input("Third number:")
                a = dependencies.check(digit1)
                b = dependencies.check(digit2)
                c = dependencies.check(digit3)
                abcformula(a, b, c)
            case _:
                print("Invalid input please try again")
