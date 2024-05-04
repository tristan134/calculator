from logic_folder import dependencies
file = "../calculator.txt"


def write_list(resultlist):
    try:
        print("Started writing list data into a txt file")
        with open(file, "a") as wfile:
            wfile.write(str(resultlist) + "\n")
            print("All results are saved in calculator.txt")
            print("The list will be cleared")
            del dependencies.elements[:]
    except FileNotFoundError:
        print("File could not be found")
    except Exception as e:
        print("An error occurred while writing", e)
        return None


def read_list():
    try:
        with open(file, 'r') as rfile:
            readfile = rfile.readlines()
            return readfile
    except FileNotFoundError:
        print("File could not be found")
        return None
    except Exception as e:
        print("An error occurred while reading", e)
        return None


def save_file():
    cancel = False
    while not cancel:
        print("1. Save results in textfile")
        print("2. Read results from textfile")
        print("3. Exit")
        choice = input("Menu: ")
        if choice == "3" or choice not in {"1", "2"}:
            break
        match choice:
            case "1":
                write_list(dependencies.elements)
            case "2":
                print(read_list())
            case _:
                print("Invalid input please try again")
