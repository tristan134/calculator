from logic_folder import dependencies


def addition(number1, number2):
    add = number1 + number2
    print("Result =", add)
    dependencies.elements.append(add)


def subtraction(number1, number2):
    sub = number1 - number2
    print("Result =", sub)
    dependencies.elements.append(sub)


def multiplication(number1, number2):
    mul = number1 * number2
    print("Result =", mul)
    dependencies.elements.append(mul)


def division(number1, number2):
    try:
        div = number1 / number2
        print("Result =", div)
        dependencies.elements.append(div)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError as v:
        print("Invalid Value", v)
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
        "1": (addition, ["Input first number: ", "Input second number: "]),
        "2": (subtraction, ["Input first number: ", "Input second number: "]),
        "3": (multiplication, ["Input first number: ", "Input second number: "]),
        "4": (division, ["Input first number: ", "Input second number: "]),
    }

    while True:
        print("\n1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. Exit")

        choice = input("Menu: ")
        print("")

        action, param_names = menu_options.get(choice, (None, []))

        if choice == "5":
            break
        if action:
            params = get_parameters(param_names)
            action(*params)
        else:
            print("Invalid choice. Please select a valid option.")
