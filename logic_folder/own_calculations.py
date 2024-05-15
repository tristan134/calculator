from logic_folder import dependencies


def own_calculation(calculation):
    global result
    try:
        result = eval(calculation)
    except Exception as e:
        print("An Error occurred:", e)
    return result


def calculate_with_last_result(last, calculation):
    global result
    try:
        test = str(last) + calculation
        result = eval(test)
    except Exception as e:
        print("An Error occurred:", e)
    return result


def main():
    global last_result
    global result_array
    last_result = 0
    result_array = []
    cancel = False
    while not cancel:
        print("\n1. Input your own calculation")
        print("2. Calculate with your last result (start your equation with an operator)")
        print("3. Print the last result")
        print("4. Choose one of the last 10 results, with you want to calculate again")
        print("5. Exit")
        choice = input("Menu: ")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break
        match choice:
            case "1":
                calculation = input("Input your equation: ")
                last_result = own_calculation(calculation)
                print(f"The result of {calculation} is: {own_calculation(calculation)}")
                result_array.append(own_calculation(calculation))
            case "2":
                calculation = input("Input your equation: ")
                print(
                    f"The result of {last_result}{calculation} is: {calculate_with_last_result(last_result, calculation)}")
                last_result = calculate_with_last_result(last_result, calculation)
                result_array.append(calculate_with_last_result(last_result, calculation))
            case "3":
                print("Your last result was: ", last_result)
            case "4":
                print("Your last results are: ", result_array)
                choice = input("Which result would you like to calculate again?: ")
                menu = dependencies.check(choice)
                menu -= 1
                print(f"{result_array[menu]} is now your last result. Choose menu number 2. to calculate again. "
                      f"Otherwise it will be overwritten.")
                last_result = result_array[menu]
            case _:
                print("Invalid input please try again")
