
elements = []


def check(value):
    if value.startswith('-') and value[1:].isdigit():
        number = int(value)
        return number
    elif value.isdigit():
        number = int(value)
        return number
    else:
        return 0
