from logic_folder import dependencies
from logic_folder import operations
from logic_folder import formulas
from logic_folder import file_handler


print("\n----------------------------")
print("Calculator MathPower III")
print("----------------------------")

if __name__ == '__main__':
    while True:
        print("\n1. Basic arithmetic operations")
        print("2. Formulas")
        print("3. Read or write a file")
        print("4. Exit")
        choice = input("Menu: ")
        menu = dependencies.check(choice)
        if menu > 4 or menu < 1:
            print("Invalid option")
        elif menu in {1, 2, 3, 4}:
            if menu == 1:
                operations.operations()
            elif menu == 2:
                print("\n1. Binomial formulas")
                print("2. Square formulas")
                print("3. Exit")
                choice = input("Menu: ")
                match choice:
                    case "1":
                        formulas.binomial()
                    case "2":
                        formulas.squareform()
                    case "3":
                        print("Exit.")
                    case _:
                        print("Invalid input please try again")
            elif menu == 3:
                file_handler.save_file()
            elif menu == 4:
                break

print("\nBye.")
