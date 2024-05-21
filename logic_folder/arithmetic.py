from logic_folder import dependencies
import math


def gcd(m, n):
    """Calculate the greatest common divisor."""
    liste = [m, n]
    liste.sort()
    print(liste)
    while liste[1] % liste[0] != 0:
        division = math.floor(liste[1] / liste[0])
        rest = liste[1] - division * liste[0]
        print(f"{liste[1]} / {liste[0]} = {division} * {liste[0]} + {rest}")
        liste[1] = liste[0]
        liste[0] = rest
    print(f"ggT: {liste[0]}")


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
        "1": (gcd, ["Input m: ", "Input n:"]),
        # "2": (function_placeholder, ["x", "y"]),
        # "3": (function_placeholder, ["x", "y"]),
        # "4": (function_placeholder, ["x", "y"]),
    }

    while True:
        print("\n1. Greatest common divisor")
        print("2. will be implemented...")
        print("3. will be implemented...")
        print("4. will be implemented...")
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
