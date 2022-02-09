from fraction import Fraction


def input_equation():
    while True:
        result = parse_linear_equation(input('> '))
        if result:
            return result
        print("Couldn't have parsed an equation provided. Please try again fulfilling the rules listed before.")


def parse_linear_equation(eq_string: str) -> list:
    def convert_to_float(start_idx, end_idx):
        val = ''.join(eq_string[start_idx:end_idx].split())
        if len(val) == 1:
            if val == '-':
                return -1.
            if val in {'', '+'}:
                return 1.
        return float(val)

    last_var_idx = 0
    params = [0.] * 3
    for i in range(len(eq_string)):
        if eq_string[i] == 'x':
            params[0] = convert_to_float(last_var_idx, i)
            last_var_idx = i+1
        elif eq_string[i] == 'y':
            params[1] = convert_to_float(last_var_idx, i)
            last_var_idx = i+1
        elif eq_string[i] == '=':
            last_var_idx = i+1
            break
    params[2] = convert_to_float(last_var_idx, None)
    return params


def system_of_equations() -> '(x, y)':
    print('''Please type in equation fulfilling the rule:
    ax + by = c
where:
    a, b, c - parameters (replace with any real numbers)
    x, y - variables (do not use other letters)
''')
    a1, b1, c1 = input_equation()
    a2, b2, c2 = input_equation()

    W = a1 * b2 - b1 * a2
    W_x = c2 * b1 - c1 * b2
    W_y = a1 * c2 - c1 * a2

    if W == 0:
        if W_x == W_y == 0:
            return float('inf'), float('inf')
        else:
            return None, None

    x = Fraction(W_x) / W
    y = Fraction(W_y) / W
    return x, y


if __name__ == '__main__':
    print(*system_of_equations())

'''
5x - 6y = 12
-2x - 6y = 12

2x + 6.25y = -4.5
8.3x - 2.15y = 18

2x + y = 1
5x = 3

2x + 8y = 12
-x - 4y = -6

2x + y = 6
6x + 3y = 1
'''
