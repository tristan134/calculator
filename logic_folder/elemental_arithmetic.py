from logic_folder import dependencies


def addition(number1, number2):
    add = number1 + number2
    print("Result=", add)
    dependencies.elements.append(add)


def subtraction(number1, number2):
    sub = number1 - number2
    print("Result=", sub)
    dependencies.elements.append(sub)


def multiplication(number1, number2):
    mul = number1 * number2
    print("Result=", mul)
    dependencies.elements.append(mul)


def division(number1, number2):
    try:
        div = number1 / number2
        print("Result=", div)
        dependencies.elements.append(div)
    except ZeroDivisionError:
        print("Not divisible by zero")
        return None
    except ValueError as v:
        print("Invalid Value", v)
        return None
    except Exception as e:
        print("Operation Error:", e)
        return None


def main():
    while True:
        print("\n1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. Exit")
        choice = input("Menu: ")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break
        num1 = dependencies.check(input("\nFirst number: "))
        num2 = dependencies.check(input("Second number: "))
        match choice:
            case "1":
                addition(num1, num2)
            case "2":
                subtraction(num1, num2)
            case "3":
                multiplication(num1, num2)
            case "4":
                division(num1, num2)
            case _:
                print("Invalid input please try again")
