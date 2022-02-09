def base_converter() -> 'to_base function':
    """Returns number system converting function"""
    values = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def to_base(num: int, base: 'int from 2 to 36' = 2) -> str:
        """Converts a 'num' number from decimal to the specified base"""
        if base == 10 or num == 0:
            return str(num)

        power = 0
        while base ** power <= num:
            power += 1
        power -= 1

        result = []
        while power >= 0:
            mul = base ** power
            for i in range(base):
                if (i+1) * mul > num:
                    break
            num -= i * mul
            power -= 1
            result.append(values[i])

        return ''.join(result)
    return to_base


to_base = base_converter()


def to_bin(num: int) -> str:
    """Converts a 'num' number from the decimal to the binary system"""
    return to_base(num, 2)


def is_palindrome(string: str) -> bool:
    """Checks if the specified string is a palindrome or not"""
    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            return False
    return True


if __name__ == '__main__':
    # e.g. check for 427, 3, 15
    num = input('> ')
    print(f'{num} is {"" if is_palindrome(num) else "not "}a palindrome')
    bin_num = to_bin(int(num))
    print(f'{bin_num} is {"" if is_palindrome(bin_num) else "not "}a palindrome')
