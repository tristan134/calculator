from logic_folder import dependencies

results = []
last_result = 0


def own_calculation(calculation):
    global temp
    try:
        temp = eval(calculation)
    except Exception as e:
        print("An Error occurred:", e)
    return temp


def calculate_with_last_result(last, calculation):
    global temp
    try:
        evaluation = str(last) + calculation
        temp = eval(evaluation)
    except Exception as e:
        print("An Error occurred:", e)
    return temp


def result_array(result, array=None):
    if array is None:
        array = results
    if len(array) <= 9:
        array.append(result)
    else:
        array.pop(0)
        array.append(result)
    return array


def main():
    global results
    global last_result
    while True:
        print("\n1. Do your own calculation")
        print("2. Calculate with your last result")
        print("3. Print the last result")
        print("4. Choose one of the last 10 results, with you want to calculate again")
        print("5. Exit")
        choice = input("Menu: ")
        print("")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break
        match choice:
            case "1":
                while True:
                    calculation = input("Input calculation (q for quit): ")
                    if calculation == "q":
                        break
                    else:
                        last_result = own_calculation(calculation)
                        print(f"The result of {calculation} is: {own_calculation(calculation)}\n")
                        result_array(own_calculation(calculation))
            case "2":
                calculation = input("Your equation has to start with an operator: ")
                print(f"The result of {last_result}{calculation} is: "
                      f"{calculate_with_last_result(last_result, calculation)}")
                last_result = calculate_with_last_result(last_result, calculation)
                result_array(calculate_with_last_result(last_result, calculation))
            case "3":
                print("Your last result is: ", last_result)
            case "4":
                if len(results) == 0:
                    print("There are no results in your history")
                else:
                    print(f"Your last results are: {results}")
                    choice = input("Which result would you like to calculate again?: ")
                    menu = dependencies.check(choice)
                    menu -= 1
                    if menu >= len(results):
                        print("Index is out of range")
                    else:
                        print(f"{results[menu]} is now your last result. Choose menu number 2. to calculate again. "
                              f"Otherwise it will be overwritten.")
                        last_result = results[menu]
            case _:
                print("Invalid input please try again")
