system_digits = '0123456789abcdef'


def to_base(num: int, base: 'int in range 2-16') -> str:
    """Converts a number num from the decimal system to the specified base"""
    if base < 2 or base > 16:
        raise ValueError('Conversion to the unsupported base ({})'.format(base))
    if base == 10 or num == 0:
        return str(num)

    result = []

    base_pow = 1
    while base_pow < num:
        base_pow *= base

    while base_pow > 0:
        mul = num // base_pow
        num -= mul * base_pow
        base_pow //= base
        result.append(system_digits[mul])

    return ''.join(result)


if __name__ == '__main__':
    # num = int(input('(integer number) > '))
    # base = int(input('(target base) > '))
    # print(to_base(num, base))
    print(to_base(100, 2))