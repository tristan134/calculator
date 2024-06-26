from logic_folder import dependencies


def input_list():
    """Generates a list of elements"""
    sortedlist = []
    amount = input("Insert the amount of numbers?: ")
    length = dependencies.check(amount)
    for i in range(0, length):
        element1 = input("Numbers: ")
        element2 = dependencies.check(element1)
        sortedlist.append(element2)
    print("Your list is: ", sortedlist)
    return sortedlist


def selection_sort(unsorted_list):
    """Sorting an unsorted list with the selection sort algorithm."""
    s = []
    u = unsorted_list
    for i in range(0, len(unsorted_list)):
        smallest = min(u)
        pos_smallest = u.index(smallest)
        s.append(smallest)
        u.pop(pos_smallest)
    print("\nThe sorted list is: ", s)


def insertion_sort(unsorted_list):
    """Sorting an unsorted list with the insertion sort algorithm."""
    s = []
    u = unsorted_list
    s.append(unsorted_list[0])
    for i in range(0, len(unsorted_list)):
        if s[i] > u[i]:
            return 0
        else:
            s.append(u[i])
    print("\nThe sorted list is: ", s)


def bubble_sort(unsorted_list):
    """Sorting an unsorted list with the bubble sort algorithm."""
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    print("\nThe sorted list is: ", unsorted_list)

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
        "1": selection_sort,
        "2": insertion_sort,
        "3": bubble_sort,
        # "4": will be implemented...,
        # "5": will be implemented...,
        # "6": will be implemented...,
    }

    while True:
        print("\n1. Selection sort")
        print("2. Insertion sort")
        print("3. Bubble sort")
        print("4. ---")
        print("5. Exit")

        choice = input("Menu: ")
        print("")

        action = menu_options.get(choice)

        if choice == "5":
            break
        if action:
            if choice in {"1", "2"}:
                unsorted_list = input_list()
                action(unsorted_list)
            else:
                pass
                # Placeholder for future functions with parameters
                # params = get_parameters(param_names)
                # action(*params)
        else:
            print("Invalid choice. Please select a valid option.")
