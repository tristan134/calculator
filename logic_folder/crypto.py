from logic_folder import dependencies


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
    expo = exponent
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
            print(result)
        exponent = exponent >> 1
        base = (base * base) % modulus

    print(f"The result of {base}^{expo} mod {modulus} is: {result}")

modular_exponentiation(2, 444, 34)


def crypto():
    cancel = False
    while not cancel:
        print("\n1. Montgomery Ladder")
        print("2. Modular Exponentiation")
        print("3. ---")
        print("4. ---")
        print("5. Exit")
        choice = input("Menu: ")
        if choice == "5" or choice not in {"1", "2", "3", "4"}:
            break

        match choice:
            case "1":
                num1 = dependencies.check(input("Base: "))
                num2 = dependencies.check(input("Exponent: "))
                num3 = dependencies.check(input("Modulo: "))
                montgomery_ladder(num1, num2, num3)
            case "2":
                num1 = dependencies.check(input("Base: "))
                num2 = dependencies.check(input("Exponent: "))
                num3 = dependencies.check(input("Modulo: "))
                modular_exponentiation(num1, num2, num3)
            case "3":
                print("Will be implemented")
            case "4":
                print("Will be implemented")
            case _:
                print("Invalid input please try again")


