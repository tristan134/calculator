from logic_folder import dependencies
import math


def montgomery_ladder(base, exponent, modulo):
    """Prints every result through the montgomery ladder."""
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
    """Does modular exponentiation on a base modulo."""
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
    """Checks if a number is prime."""
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


def list_primefactors(number):
    """Lists all prime factors up to a number.
    Example: 13 is [2, 2, 2, 3, 3, 5, 7, 11 , 13]"""
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
    """Uses the p-1 method to find the gcd of two numbers."""
    result = 1
    for i in list_primefactors(k):
        result *= i
    p = (2 ** result - 1) % m
    pair = [m, p]
    pair.sort()
    print(pair)
    while pair[1] % pair[0] != 0:
        division = math.floor(pair[1] / pair[0])
        rest = pair[1] - division * pair[0]
        print(f"{pair[1]} / {pair[0]} = {division} * {pair[0]} + {rest}")
        pair[1] = pair[0]
        pair[0] = rest
    print(f"The gcd of {m} and {k} is {pair[0]}")
    return pair[0]


def order_additive_group(n, element):
    """Returns the order of an element in an additive group."""
    order = 1
    result = element % n
    while result != 0:
        result = (result + element) % n
        order += 1
    print(f"The order is {order}")
    return order


def order_multiplicative_group(n, element):
    """Returns the order of an element in a multiplicative group."""
    if element == 0:
        return float('inf')
    order = 1
    result = element % n
    while result != 1:
        result = (result * element) % n
        order += 1
        if order > n:
            return None
    print(f"The order is {order}")
    return order


def diffie_hellman(p, g, a, b):
    """Generates a private key for Alice and Bob each and their public key"""
    if a < p and b < p:
        order = order_multiplicative_group(p, g)
        if is_prime(order):
            print(f"The order of {g} in {p} is prime ({order}), that's good!")
        else:
            print(f"The order of {g} in {p} is not prime ({order}), but it should be for security reasons!")
        alpha = (g**a) % p
        beta = (g**b) % p
        beta_alpha = (g**(b*a)) % p
        alpha_beta = (g**(a*b)) % p
        if beta_alpha == alpha_beta:
            print(f"Alice' private key is {alpha}")
            print(f"Bob's private key is {beta}")
            print(f"The public key of Alice and Bob is {alpha_beta}")
        else:
            print(f"The public key of Alice and Bob is not equal. Something went wrong!")
    else:
        print("Please pick random numbers for a and b < p!")


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
        "1": (montgomery_ladder, ["Base: ", "Exponent: ", "Modulo: "]),
        "2": (modular_exponentiation, ["Base: ", "Exponent: ", "Modulo: "]),
        "3": (p_minus_1_method, ["Input m: ", "Input k: "]),
        "4": (diffie_hellman, ["Group: ", "Element: ", "Random number(a) for Alice (<p): ", "Random number(b) for Bob (<p): "]),
        "5": (order_additive_group, ["Group: ", "Element: "]),
        "6": (order_multiplicative_group, ["Group: ", "Element: "]),
    }

    while True:
        print("\n1. Montgomery Ladder")
        print("2. Modular Exponentiation")
        print("3. P-1 Method")
        print("4. Diffie-Hellman Method")
        print("5. Determine the order of an element in a additive group")
        print("6. Determine the order of an element in an multiplicative group")
        print("7. Exit")

        choice = input("Menu: ")
        print("")

        action, param_names = menu_options.get(choice, (None, []))

        if choice == "7":
            break
        if action:
            params = get_parameters(param_names)
            action(*params)
        else:
            print("Invalid choice. Please select a valid option.")
