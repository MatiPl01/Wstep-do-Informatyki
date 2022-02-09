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


base_fns = {
    2: bin,
    8: oct,
    16: hex
}

checked = 0
passed = 0
to_base = base_converter()
for base in [2, 8, 16]:
    for num in range(1000):
        checked += 1
        my_fn_res = to_base(base, num)
        built_in_fn_res = base_fns[base](num)[2:]
        print(my_fn_res, built_in_fn_res)
        if my_fn_res == built_in_fn_res:
            passed += 1
        else:
            print('wrong', num, my_fn_res, built_in_fn_res)

print(checked, passed)
