import formulas
import dependencies
import operations
import file_handler



print("\n----------------------------")
print("Calculator MathPower III")
print("----------------------------")




while True:
    print("")
    print("1. Basic arithmetic operations")
    print("2. Formulas")
    print("3. Miscellaneous")
    print("4. Exit")
    choice = input("Menu: ")
    menu = dependencies.check(choice)
    if menu > 4 or menu < 1:
        print("Invalid option")
    elif menu in {1, 2, 3, 4}:
        if menu == 1:
            operations.operations()
        elif menu == 2:
            formulas.formulas()
        elif menu == 3:
            file_handler.save_file()
        elif menu == 4:
            break

print("\nBye.")
