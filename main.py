from logic_folder import dependencies
from logic_folder import elemental_arithmetic
from logic_folder import elemental_algebra
from logic_folder import file_handler
from logic_folder import crypto


print("\n----------------------------")
print("Calculator MathPower III")
print("----------------------------")

if __name__ == '__main__':
    while True:
        print("\n1. Elemental arithmetic")
        print("2. Elemental algebra")
        print("3. Cryptographic algorithms")
        print("4. File access")
        print("5. Exit")
        choice = input("Menu: ")
        menu = dependencies.check(choice)
        if menu > 6 or menu < 1:
            print("Invalid option")
        elif menu in {1, 2, 3, 4, 5, 6}:
            if menu == 1:
                elemental_arithmetic.main()
            elif menu == 2:
                print("\n1. Binomial formulas")
                print("2. Square formulas")
                print("3. Exit")
                choice = input("Menu: ")
                match choice:
                    case "1":
                        elemental_algebra.binomial()
                    case "2":
                        elemental_algebra.squareform()
                    case "3":
                        print("")
                    case _:
                        print("Invalid input please try again")
            elif menu == 3:
                crypto.crypto()
            elif menu == 4:
                file_handler.save_file()
            elif menu == 5:
                print("Coming soon.")
            elif menu == 6:
                break

print("\nBye.")
