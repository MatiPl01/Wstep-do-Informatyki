import math
from fraction import Fraction


def type_name(obj: object) -> str:
    return str(type(obj))[8:-2]


def as_pi_part(angle: float) -> "'Fraction' instance":
    return Fraction(angle / math.pi)


def as_degrees(angle: float) -> float:
    return angle * 180 / math.pi


class Complex:
    def __init__(self, *args):
        self._real, self._imag = self.__parse_input(args)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.real}, {self.imag})'

    def __str__(self):
        imag = f"{self.imag}i" if self.imag else ""
        real = (self.real or "") if imag else self.real
        sign = "+" if self.imag > 0 and real else ""
        return f'{real}{sign}{imag}'

    def __iter__(self):
        return iter((self.real, self.imag))

    def __abs__(self):
        res = (self.real**2 + self.imag**2)**.5
        return int(res) if res == int(res) else res

    def __neg__(self):
        return Complex(-self.real, -self.imag)

    def __eq__(self, other):
        other = self.as_complex(other)
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        other = self.as_complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        other = self.as_complex(other)
        self._real += other.real
        self._imag += other.imag

    def __sub__(self, other):
        other = self.as_complex(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        other = self.as_complex(other)
        self._real -= other.real
        self._imag -= other.imag

    def __mul__(self, other):
        other = self.as_complex(other)
        x1, y1 = self
        x2, y2 = other
        return Complex(x1*x2 - y1*y2, x1*y2 + x2*y1)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self.as_complex(other)
        x1, y1 = self
        x2, y2 = other
        denominator = x2**2 + y2**2
        return Complex((x1*x2 + y1*y2)/denominator, (x2*y1 - x1*y2)/denominator)

    def __rtruediv__(self, other):
        other = self.as_complex(other)
        x1, y1 = other
        x2, y2 = self
        denominator = x2**2 + y2**2
        return Complex((x1*x2 + y1*y2)/denominator, (x2*y1 - x1*y2)/denominator)

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                result = 1
                for _ in range(power):
                    result *= self
                return result
                # return Complex.from_trigonometric(abs(self) ** power, power * self.arg())
            else:
                return 1/self**abs(power)
        elif isinstance(power, float):
            n = power**-1
            if int(n) == n:
                return self.root(int(n))
            else:
                raise ValueError(f'Cannot calculate ({self})^{power}')

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def arg(self):
        try:
            angle = math.acos(self.real / abs(self))
            return angle * -1 if self.imag < 0 else angle
        except ZeroDivisionError:
            raise ZeroDivisionError(f'Cannot calculate arg({self}) because module equals to 0')

    def root(self, index: int) -> list:
        if self == 0:
            return [self]
        if isinstance(index, float):
            n = index**-1
            if n == int(n):
                return self ** int(n)
        if not isinstance(index, int):
            raise TypeError('Cannot calculate root of a complex number of non-integral index')
        results = []
        angle = self.arg()
        module = abs(self)**(1/index)
        for k in range(index):
            angle_k = (angle + 2*k*math.pi)/index
            results.append(self.from_trigonometric(module, angle_k))
        return results

    def as_trigonometric(self, *, as_fraction=True):
        return self.to_trigonometric(abs(self), self.arg(), as_fraction=as_fraction)

    @staticmethod
    def to_trigonometric(module: float, angle: float, *, as_fraction=True) -> str:
        if as_fraction:
            angle = f'{as_pi_part(angle)}π'
        return f"{module}*(cos({angle})+i*sin({angle}))"

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    @classmethod
    def as_complex(cls, *values):
        if len(values) == 1:
            val = values[0]
            if isinstance(val, cls):
                return val
            return cls(val)
        return cls(*values)

    @staticmethod
    def __parse_value(val):
        if isinstance(val, int):
            return val
        if isinstance(val, str):
            try:
                val = float(val)
            except ValueError:
                raise ValueError(f'Wrong string value passed: {val}')
        if isinstance(val, float):
            if int(val) == val:
                return int(val)
            return val
        # If non of the ifs above returned any value, we got a wrong input
        raise TypeError(f'Wrong value passed. Got value of an unsupported type: {val} ({type_name(val)}).')

    @classmethod
    def __parse_input(cls, args):
        if len(args) > 2:
            raise ValueError(f'Expected at most 2 arguments, got {len(args)}')

        if len(args) == 1:
            value = args[0]
            if isinstance(value, cls):
                return cls(*value)
            if isinstance(value, complex):
                return (int(v) for v in (value.real, value.imag) if v == int(v))
            elif isinstance(value, str) and (value.endswith('i') or value.endswith('j')):
                value = value[:-1]
                value_parts = value.split('+')
                sign = 1
                if len(value_parts) != 2:
                    value_parts = value.split('-')
                    if len(value_parts) == 2:
                        sign = -1

                if len(value_parts) == 2:
                    if not value_parts[-1]:
                        if value_parts[0]:
                            return cls.__parse_value(value_parts[0]), sign
                        return 0, sign
                    return (cls.__parse_value(v) for v in value_parts)
                return 0, cls.__parse_value(value_parts[0]) if value_parts[0] else sign
            return cls.__parse_value(value), 0

        else:
            return (cls.__parse_value(v) for v in args)

    @classmethod
    def from_trigonometric(cls, module: float, angle: float) -> "'Complex' instance":
        real = module * math.cos(angle)
        imag = module * math.sin(angle)
        return cls(real, imag)
