from logic_folder import dependencies
import math


def montgomery_ladder(base, exponent, modulo):
    base %= modulo
    # Binary representation of exponent
    bin_exponent = list(map(int, bin(exponent)[2:]))

    r0 = 1
    r1 = base

    # Iterate through each bit of the binary exponent, starting from the most significant to the least significant
    for i in range(len(bin_exponent)):
        if bin_exponent[i] == 0:
            r1 = (r1 * r0) % modulo
            r0 = (r0 ** 2) % modulo
            print(f"Intermediate result: x={r0} and y={r1}")
        else:
            r0 = (r0 * r1) % modulo
            r1 = (r1 ** 2) % modulo
            print(f"Intermediate result: x={r0} and y={r1}")
    print(f"The result of {base}^{exponent} mod {modulo} is: {r0}")


def modular_exponentiation(base, exponent, modulus):
    result = 1
    pexponent = exponent
    pbase = base
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    print(f"The result of {pbase}^{pexponent} mod {modulus} is: {result}")


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_with_exponent(number):
    result = []
    i = 2
    while True:
        if is_prime(i):
            exponent = 1
            while i ** exponent <= number:
                result.append(i)
                exponent += 1
        if i > number:
            break
        i += 1
    return result


def p_minus_1_method(m, k):
    result = 1
    for i in prime_with_exponent(k):
        result *= i
    p = (2 ** result - 1) % m
    liste = [m, p]
    liste.sort()
    print(liste)
    while liste[1] % liste[0] != 0:
        division = math.floor(liste[1] / liste[0])
        rest = liste[1] - division * liste[0]
        print(f"{liste[1]} / {liste[0]} = {division} * {liste[0]} + {rest}")
        liste[1] = liste[0]
        liste[0] = rest
    print(f"ggT: {liste[0]}")


def diffie_hellman(n, m):
    pass


def main():
    while True:
        print("\n1. Montgomery Ladder")
        print("2. Modular Exponentiation")
        print("3. P-1 Method")
        print("4. ---")
        print("5. Exit")
        choice = input("Menu: ")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break
        match choice:
            case "1":
                num1 = dependencies.check(input("\nBase: "))
                num2 = dependencies.check(input("Exponent: "))
                num3 = dependencies.check(input("Modulo: "))
                montgomery_ladder(num1, num2, num3)
            case "2":
                num1 = dependencies.check(input("\nBase: "))
                num2 = dependencies.check(input("Exponent: "))
                num3 = dependencies.check(input("Modulo: "))
                modular_exponentiation(num1, num2, num3)
            case "3":
                num1 = dependencies.check(input("\nInput m: "))
                num2 = dependencies.check(input("Input B: "))
                p_minus_1_method(num1, num2)
            case "4":
                num1 = dependencies.check(input("\nNumber: "))
                prime_with_exponent(num1)
            case _:
                print("Invalid input please try again")
