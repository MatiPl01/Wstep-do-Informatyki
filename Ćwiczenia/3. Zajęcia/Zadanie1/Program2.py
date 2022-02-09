# Another approach, using closure

def base_converter() -> 'base converting function':
    """Returns a function that performs number conversion from decimal to specified base"""
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'

    def to_base(num: int, base: 'int in range 2-32') -> str:
        """Converts a number num from the decimal system to the specified base"""
        if base < 2 or base > 32:
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
            result.append(digits[mul])

        return ''.join(result)

    return to_base


if __name__ == '__main__':
    to_base = base_converter()
    num = int(input('(integer number) > '))
    base = int(input('(target base) > '))
    print(to_base(num, base))
