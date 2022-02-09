# Fully class-based solution
"""
10. Liczby naturalne reprezentowane jak poprzednim zadaniu.
Proszę napisać funkcję dodającą dwie takie liczby.
W wyniku dodawania dwóch liczb powinna powstać nowa lista.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class NaturalNumber:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = self.tail = None
        self.length = 0

        self.__initialize(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.initial_value})"

    def __str__(self):
        return ''.join(str(v) for v in self)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self.length

    def __int__(self):
        self_iterator = iter(self)
        result = next(self_iterator)
        for digit in self_iterator:
            result = 10*result + digit
        return result

    def __add__(self, other):
        if isinstance(other, self.__class__):
            self_pointer = self.tail
            other_pointer = other.tail

            # Initialise a result instance with the last digit
            rest, digit = divmod(self_pointer.value + other_pointer.value, 10)
            ll_result = self.__class__(digit)
            self_pointer = self_pointer.prev
            other_pointer = other_pointer.prev

            # Sum subsequent digits of both numbers till both pointers aren't exhausted
            while self_pointer and other_pointer:
                rest, digit = divmod(self_pointer.value + other_pointer.value + rest, 10)
                ll_result.prepend(digit)

                self_pointer = self_pointer.prev
                other_pointer = other_pointer.prev

            # If there are still some digits in the self_pointer (other_pointer is exhausted)
            if self_pointer:
                self.__fill_remaining_values(ll_result, self_pointer, rest)
            elif other_pointer:
                self.__fill_remaining_values(ll_result, other_pointer, rest)
            elif rest:
                # If there is still some rest (this happens when both pointers were exhausted at the same time)
                ll_result.prepend(rest)

            return ll_result

        elif isinstance(other, int):
            return self + self.__class__(other)

        else:
            cls = self.__class__.__name__
            raise TypeError(f"Can only add 'int' and '{cls}' instance to '{cls}', not {str(type(other))[7:-1]}")

    def __radd__(self, other):
        return self + other

    def append(self, value):
        node = Node(value)
        if self:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def prepend(self, value):
        node = Node(value)
        if self:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def __initialize(self, value):
        if value is None:
            value = 0
        if isinstance(value, int):
            if value == 0:
                self.append(value)
            elif value > 0:
                while value:
                    value, digit = divmod(value, 10)
                    self.prepend(digit)
            else:
                raise ValueError(f"Expected a non-negative 'int', got {value}.")

        elif isinstance(value, self.__class__):
            self.extend(value)
        else:
            raise TypeError(f"Expected 'int' or '{self.__class__.__name__}' instance, got {str(type(value))[7:-1]}.")

    @staticmethod
    def __fill_remaining_values(ll_result, pointer, rest):
        while pointer:
            if rest:
                rest, digit = divmod(pointer.value + rest, 10)
                ll_result.prepend(digit)
            else:
                ll_result.prepend(pointer.value)
            pointer = pointer.prev

        # There still can be some rest
        if rest:
            ll_result.prepend(rest)


if __name__ == '__main__':
    # a = 4
    # b = 3
    a = 12345
    b = 87655
    # a = 5
    # b = 99995
    num_a = NaturalNumber(NaturalNumber(a))
    print(repr(num_a), num_a)
    num_b = NaturalNumber(b)
    print(num_b)
    print(num_a + num_b)
    print(len(num_a))
    print(num_a + 655)
    print(655 + num_a)
    print(int(num_a) / 2)
    # print(num_a / 2)  # This one won't work as NaturalNumber instance doesn't support division
    print(int(NaturalNumber(int(NaturalNumber(int(NaturalNumber(int(NaturalNumber()))))))))
    # print(repr(NaturalNumber(NaturalNumber(NaturalNumber(NaturalNumber())))))
