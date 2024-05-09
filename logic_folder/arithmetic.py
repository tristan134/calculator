from logic_folder import dependencies
import math


def gcd(m, n):
    liste = [m, n]
    liste.sort()
    print(liste)
    while liste[1] % liste[0] != 0:
        division = math.floor(liste[1] / liste[0])
        rest = liste[1] - division * liste[0]
        print(f"{liste[1]} / {liste[0]} = {division} * {liste[0]} + {rest}")
        liste[1] = liste[0]
        liste[0] = rest
    print(f"ggT: {liste[0]}")




def main():
    cancel = False
    while not cancel:
        print("\n1. Greatest common divisor")
        print("2. ---")
        print("3. ---")
        print("4. ---")
        print("5. Exit")
        choice = input("Menu: ")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break

        match choice:
            case "1":
                num1 = dependencies.check(input("\nNumber 1: "))
                num2 = dependencies.check(input("Number 2: "))
                gcd(num1, num2)
            case "2":
                print("Will be implemented")
            case "3":
                print("Will be implemented")
            case "4":
                print("Will be implemented")
            case _:
                print("Invalid input please try again")

