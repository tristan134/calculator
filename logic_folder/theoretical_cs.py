from logic_folder import dependencies


def input_list():
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
    s = []
    u = unsorted_list
    for i in range(0, len(unsorted_list)):
        smallest = min(u)
        pos_smallest = u.index(smallest)
        s.append(smallest)
        u.pop(pos_smallest)
    print("\nThe sorted list is: ", s)


def insertion_sort(unsorted_list):
    s = []
    u = unsorted_list
    s.append(unsorted_list[0])
    for i in range(0, len(unsorted_list)):
        if s[i] > u[i]:
            return 0
        else:
            s.append(u[i])
    print("\nThe sorted list is: ", s)


def main():
    while True:
        print("\n1. Selection sort")
        print("2. Insertion sort")
        print("3. ---")
        print("4. ---")
        print("5. Exit")
        choice = input("Menu: ")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break
        match choice:
            case "1":
                selection_sort(input_list())
            case "2":
                insertion_sort(input_list())
            case "3":
                print("Will be implemented")
            case "4":
                print("Will be implemented")
            case _:
                print("Invalid input please try again")
