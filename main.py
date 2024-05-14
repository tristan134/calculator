from logic_folder import dependencies
from logic_folder import elemental_arithmetic
from logic_folder import elemental_algebra
from logic_folder import file_handler
from logic_folder import crypto
from logic_folder import arithmetic
from logic_folder import theoretical_cs
from logic_folder import own_calculations

print("\n----------------------------")
print("Calculator MathPower III")
print("----------------------------")

if __name__ == '__main__':
    while True:
        print("\n1. Own calculations")
        print("2. Elemental arithmetic")
        print("3. Arithmetic")
        print("4. Elemental algebra")
        print("5. Cryptographic algorithms")
        print("6. Theoretical computer science")
        print("7. File access")
        print("8. Exit")
        choice = input("Menu: ")
        menu = dependencies.check(choice)
        if menu > 7 or menu < 1:
            print("Invalid option")
        elif menu in {1, 2, 3, 4, 5, 6, 7}:
            if menu == 1:
                own_calculations.main()
            elif menu == 2:
                elemental_arithmetic.main()
            elif menu == 3:
                arithmetic.main()
            elif menu == 4:
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
            elif menu == 5:
                crypto.main()
            elif menu == 6:
                theoretical_cs.main()
            elif menu == 7:
                file_handler.save_file()
            elif menu == 8:
                break

print("\nBye.")
