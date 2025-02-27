from ops.math import *


def validate(exp):
    chars = '+-*^/'
    nums = '0123456789.'
    ops = []
    val_exp = ['']
    for i, char in enumerate(exp.replace(' ','')):
        if char in chars:
            if char == '-' and (i == 0 or exp[i - 1] in chars):
                val_exp[-1] += char
            else:
                ops.append(char)
                val_exp.append('')
                val_exp[-1] += char
                val_exp.append('')
        elif char in nums:
            val_exp[-1] += char
        else:
            print(f"Недопустимый символ: {char}")
            return
    if val_exp[-1] in chars:
        print("Ошибка: выражение не может заканчиваться на оператор.")
        return
    #print('\texp:', *val_exp, '\n\tops:', *ops)
    return val_exp


def calculate(exp):
    for i in range(len(exp)):
        if exp[i].replace('.', '', 1).lstrip('-').isdigit():
            exp[i] = float(exp[i])

    ops_order = ['^', '*/', '+-']
    for ops in ops_order:
        i = 0
        while i < len(exp):
            if isinstance(exp[i], str) and exp[i] in ops:
                a, op, b = exp[i - 1], exp[i], exp[i + 1]
                if op == '^':
                    result = power(a, b)
                elif op == '*':
                    result = multiply(a, b)
                elif op == '/':
                    result = divide(a, b)
                elif op == '+':
                    result = add(a, b)
                elif op == '-':
                    result = subtract(a, b)
                else:
                    i += 1
                    continue

                exp = exp[:i - 1] + [result] + exp[i + 2:]
                #print(*exp)
                i -= 1
            else:
                i += 1

    if isinstance(exp, list) and len(exp) == 1:
        result = exp[0]
    else:
        result = None
    #print(f'result = {result}')
    return result


def calc(exp):
    exp = validate(exp)
    if exp is None:
        return
    return calculate(exp)
