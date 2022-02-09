class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


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
            if value >= 0:
                for _ in range(value):
                    self.append(None)
            else:
                raise ValueError(f"Expected a positive integer, got {value}.")
        elif hasattr(value, '__iter__'):
            self.extend(value)
        else:
            raise TypeError(f"Expected an iterable or 'int', got {str(type(value))[7:-1]}.")


def get_number(ll: LinkedList) -> int:
    res = 0
    curr = ll.tail

    mul = 1
    while curr:
        res += curr.value * mul
        mul *= 10
        curr = curr.prev

    return res


def add_one(ll: LinkedList):
    curr = ll.tail
    rest = 1

    while curr and rest:
        rest, digit = divmod(curr.value + rest, 10)
        curr.value = digit
        if not rest:
            break
        curr = curr.prev

    if rest:  # If there is still a rest remaining, prepend this number to the beginning of the linked list
        ll.prepend(rest)


if __name__ == '__main__':
    # digits = 9,
    digits = 9, 9, 9, 9, 9, 9, 9
    # digits = 8, 9, 9, 7, 9, 9
    digits_ll = LinkedList(digits)
    print(digits_ll)
    print(get_number(digits_ll))
    add_one(digits_ll)
    print(digits_ll)
    print(get_number(digits_ll))
