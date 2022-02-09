def type_name(obj: object) -> str:
    return str(type(obj))[8:-2]


def gcd(a: int, b: int) -> int:
    return a if not b else gcd(b, a % b)


def as_integer_ratio(num) -> tuple:
    num_parts = str(num).split('.')
    int_part, float_part = map(lambda v: int(v), num_parts)
    sign = -1 if int_part < 0 else 1
    denominator = 10 ** (len(num_parts[1]))
    numerator = sign * (abs(int_part) * denominator + float_part)
    return numerator, denominator


class Fraction:
    def __init__(self, *args):
        self._numerator, self._denominator = self.simplify(*self.__parse_input(*args))

    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __iter__(self):
        return iter((self.numerator, self.denominator))

    def __add__(self, other):
        other = self.as_fraction(other)
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self.as_fraction(other)
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other):
        other = self.as_fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self.as_fraction(other)
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __rtruediv__(self, other):
        other = self.as_fraction(other)
        return Fraction(other.numerator * self.denominator, other.denominator * self.numerator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def __int__(self):
        return int(self.numerator / self.denominator)

    def __float__(self):
        return self.numerator / self.denominator

    def __eq__(self, other):
        other = self.as_fraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        other = self.as_fraction(other)
        return not self == other

    def __lt__(self, other):
        other = self.as_fraction(other)
        if self.denominator == other.denominator:
            return self.numerator < other.numerator
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        other = self.as_fraction(other)
        if self.denominator == other.denominator:
            return self.numerator > other.numerator
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                return Fraction(self.numerator ** power, self.denominator ** power)
            else:
                power = abs(power)
                return Fraction(self.denominator ** power, self.numerator ** power)
        else:
            if isinstance(power, Fraction):
                power = float(power)
            numerator_pow = Fraction(*as_integer_ratio(self.numerator ** power))
            denominator_pow = Fraction(*as_integer_ratio(self.denominator ** power))
            return numerator_pow / denominator_pow

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, num):
        if isinstance(num, int):
            self._numerator = num
            self.simplify_update()
        elif isinstance(num, float) or isinstance(num, str):
            self._numerator, self._denominator = Fraction(num) / self

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, num):
        self._numerator, self._denominator = self.numerator * Fraction(num)**-1

    @staticmethod
    def as_fraction(value):
        if not isinstance(value, Fraction):
            return Fraction(value)
        return value

    @classmethod
    def __parse_input(cls, *args):
        if len(args) > 2:
            raise ValueError(f'Expected at most 2 values, got {len(args)}.')
        if len(args) == 1:
            num = args[0]
            if isinstance(num, cls):
                return num.numerator, num.denominator
            if isinstance(num, int):
                return num, 1
            if isinstance(num, float):
                numerator, denominator = as_integer_ratio(num)
            elif isinstance(num, str):
                # If passed fraction where numerator and denominator are separated by /
                num_parts = num.split('/')
                try:
                    if len(num_parts) == 2:
                        numerator, denominator = map(lambda v: int(v), num_parts)
                    else:
                        # Handle cases in which number is float where a fixed point is separated by comma
                        # or by dot from a floating point
                        numerator, denominator = as_integer_ratio(num.replace(',', '.'))
                except ValueError:
                    raise ValueError(f"Invalid string value passed. Please make sure you"
                                     f"haven't repeated any of signs listed: '.,/'.")
        else:
            if isinstance(args[0], int) and isinstance(args[1], int):
                numerator, denominator = args
            else:
                raise ValueError(f'Expected two integers, got {type_name(args[0])} and {type_name(args[1])}.')
        if denominator == 0:
            raise ZeroDivisionError(f"Division by zero is not supported.")
        return numerator, denominator

    @staticmethod
    def simplify(numerator: int, denominator: int) -> tuple:
        div = gcd(numerator, denominator)
        numerator //= div
        denominator //= div
        return numerator, denominator

    def simplify_update(self):
        self._numerator, self._denominator = self.simplify(self._numerator, self._denominator)
