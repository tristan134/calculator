from logic_folder import dependencies
from logic_folder import elemental_arithmetic
from logic_folder import elemental_algebra
from logic_folder import file_handler
from logic_folder import crypto
from logic_folder import arithmetic
from logic_folder import theoretical_cs
from logic_folder import own_calculations




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


if __name__ == '__main__':
    print("\n----------------------------")
    print("Calculator MathPower III")
    print("----------------------------")
    menu_options = {
        "1": (own_calculations.main, []),
        "2": (elemental_arithmetic.main, []),
        "3": (arithmetic.main, []),
        "4": (elemental_algebra.main, []),
        "5": (crypto.main, []),
        "6": (theoretical_cs.main, []),
        # "7": file_handler.save_file, []),
    }

    while True:
        print("\n1. Own calculations")
        print("2. Elemental arithmetic")
        print("3. Arithmetic")
        print("4. Elemental algebra")
        print("5. Cryptographic algorithms")
        print("6. Theoretical computer science")
        print("7. File access (Not working right now)")
        print("8. Exit")

        choice = input("Menu: ")
        print("")

        action, param_names = menu_options.get(choice, (None, []))

        if choice == "8":
            break
        if action:
            action(*param_names)
        else:
            print("Invalid choice. Please select a valid option.")

print("\nBye.")
