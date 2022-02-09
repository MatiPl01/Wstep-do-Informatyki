def get_base_digits_init() -> "'to_base' function":
    digits = '0123456789abcdefghijklmnopqrstuywxuz'

    def get_base_digits(num: int, base: int) -> set:
        base_digits = set()

        while num:
            num, digit = divmod(num, base)
            base_digits.add(digits[digit])

        return base_digits or {0}

    return get_base_digits


get_base_digits = get_base_digits_init()


def search_base(num1: int, num2: int) -> int:
    for base in range(2, 16):
        num1_digits = get_base_digits(num1, base)
        num2_digits = get_base_digits(num2, base)
        if not num1_digits & num2_digits:
            return base
    return -1


if __name__ == '__main__':
    num1 = int(input('(num1) > '))
    num2 = int(input('(num2) > '))
    print(search_base(num1, num2))
