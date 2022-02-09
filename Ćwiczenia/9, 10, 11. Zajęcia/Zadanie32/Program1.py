import random


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = self.tail = None
        self.length = 0

        self.__initialize(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.initial_value})"

    def __str__(self):
        return ' -> '.join(str(v) for v in self)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self.length

    def append(self, value):
        node = Node(value)
        if self:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        self.length += 1

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def __initialize(self, value):
        if value is None:
            value = 0
        if isinstance(value, int):
            if value >= 0:
                for _ in range(value):
                    self.append(None)
            else:
                raise ValueError(f"Expected a positive integer, got {value}.")
        elif hasattr(value, '__iter__'):
            self.extend(value)
        else:
            raise TypeError(f"Expected an iterable or 'int', got {str(type(value))[7:-1]}.")


def random_numbers_list(count: int, min_num: int, max_num: int) -> [int]:
    return [random.randint(min_num, max_num) for _ in range(count)]


def subtract_polynomials(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    result = LinkedList()

    ll1_iter = iter(ll1)
    ll2_iter = iter(ll2)
    for val1, val2 in zip(ll1_iter, ll2_iter):
        result.append(val1 - val2)

    for val in ll1_iter:   # If ll1 isn't yet exhausted, append remaining values
        result.append(val)

    for val in ll2_iter:   # If ll1 isn't yet exhausted, append remaining values (negative sign as we subtract them)
        result.append(-val)

    return result


def print_polynomial(ll: LinkedList):
    a_list = iter(ll)
    a0 = next(a_list)
    result = LinkedList([str(a0)])

    exponent = 1
    for a in a_list:
        result.prepend(f"{a}x^{exponent}")
        exponent += 1

    print(' + '.join(result))


if __name__ == '__main__':
    random.seed(0)
    p1 = LinkedList(random_numbers_list(6, -20, 20))
    p2 = LinkedList(random_numbers_list(10, -50, 50))
    p_res = subtract_polynomials(p1, p2)

    print('p1:', p1)
    print_polynomial(p1)
    print()

    print('p2:', p2)
    print_polynomial(p2)
    print()

    print('p_res:', p_res)
    print_polynomial(p_res)
    print()
