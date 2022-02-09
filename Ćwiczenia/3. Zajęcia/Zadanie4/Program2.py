# def divide(n: int, div: int, *, prec: int = 16) -> str:
#     """Divides 'n' by 'div' calculating up to 'prec' floating point digits"""
#     fixed_point = n // div
#     if fixed_point:
#         n %= fixed_point
#     floating_point = []
#
#     for i in range(prec):
#         n *= 10
#         if n == 0:
#             break
#         digit, n = divmod(n, div)
#         floating_point.append(str(digit))
#
#     return f'{fixed_point}.{"".join(floating_point).ljust(prec, "0") if floating_point else 0}'


def divide(n: int, div: int, *, prec: int = 16) -> (int, int, int):
    """Divides 'n' by 'div' calculating up to 'prec' floating point digits
    Returns (<fixed point>, <floating point>, <number of zeros preceding the floating point>)
    """
    fixed_point = n // div
    if fixed_point:
        n %= fixed_point
    floating_point = 0

    pow_10 = 10 ** prec
    i = 0
    while pow_10 > 0:
        n *= 10
        if n == 0:
            break
        digit, n = divmod(n, div)
        floating_point += digit * pow_10
        pow_10 //= 10
        i += 1

    return fixed_point, floating_point, prec-i


def calc_e(prec: int = 16) -> str:
    """Calculates a value of e"""
    e_fixed_point = 0
    e_floating_point = 0
    factorial = 1
    n = 1

    while True:
        # fixed_point, floating_point = (int(v) for v in divide(1, fact, prec=prec).split('.'))
        fixed_point, floating_point, preceding_zeros = divide(1, factorial, prec=prec)
        e_fixed_point += fixed_point
        e_floating_point += floating_point
        factorial *= n
        n += 1
        if not fixed_point and floating_point == 0:  # FIX
            break

    return f'{e_fixed_point}.{e_floating_point}'


if __name__ == '__main__':
    prec = int(input('> '))
    e = calc_e(prec)
    print(e)
