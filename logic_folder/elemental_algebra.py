from logic_folder import dependencies
import math


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


def get_parameters(parameter_names):
    parameters = []
    for name in parameter_names:
        while True:
            try:
                value = input(f"{name}")
                value = dependencies.check(value)
                parameters.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
    return parameters


def main():
    menu_options = {
        "1": (firstbinomial, ["Input a: ", "Input b: "]),
        "2": (secondbinomial, ["Input a: ", "Input b: "]),
        "3": (thirdbinomial, ["Input a: ", "Input b: "]),
        "4": (pqformula, ["Input p: ", "Input q: "]),
        "5": (abcformula, ["Input a: ", "Input b: ", "Input c: "]),

    }

    while True:
        print("\n1. first binomial formula (a^2+2ab+b^2)")
        print("2. second binomial formula (a^2-2ab+b^2)")
        print("3. third binomial formula (a^2-b^2)")
        print("4. pq-formula")
        print("5. abc-formula")
        print("6. Exit")

        choice = input("Menu: ")
        print("")

        action, param_names = menu_options.get(choice, (None, []))

        if choice == "6":
            break
        if action:
            params = get_parameters(param_names)
            action(*params)
        else:
            print("Invalid choice. Please select a valid option.")
