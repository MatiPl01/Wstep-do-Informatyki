def base_converter() -> 'to_base function':
    """Returns number system converting function"""
    values = '0123456789abcdefghijklmnopqrstuvwxyz'

    def to_base(base: 'int from 2 to 36', num: 'integer number in decimal system') -> str:
        """Converts a 'num' number from decimal to the specified base"""
        if base == 10 or num == 0:
            return str(num)

        # Find the lowest exponent that makes power of base greater than or equal to num
        exp = 0
        while base ** exp <= num:
            exp += 1
        exp -= 1

        # Perform number base conversion
        result = []
        while exp >= 0:
            mul = base ** exp
            for i in range(base):
                if (i + 1) * mul > num:
                    break
            num -= i * mul
            exp -= 1
            result.append(values[i])

        return ''.join(result)
    return to_base


to_base = base_converter()


if __name__ == '__main__':
    a = input('> ')
    b = input('> ')
    a_cp = int(a)
    b_cp = int(b)
    min_base = 2
    max_base = 11

    # If numbers still have
    for base in range(min_base, max_base+1):
        a = to_base(base, a_cp)
        b = to_base(base, b_cp)

        if not (set(a) & set(b)):
            print(base)
            break
    else:
        print('No proper base found')
