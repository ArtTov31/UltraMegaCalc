def add(a, b):
    return eval(f'{a} + {b}')


def subtract(a, b):
    return eval(f'{a} - {b}')


def multiply(a, b):
    return eval(f'{a} * {b}')


def divide(a, b):
    try:
        return eval(f'{a} / {b}')
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return ZeroDivisionError


def power(a, b):
    return eval(f'{a}**{b}')
