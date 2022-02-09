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


def add_numbers(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    ll1_pointer = ll1.tail
    ll2_pointer = ll2.tail
    ll_result = LinkedList()
    rest = 0

    while ll1_pointer and ll2_pointer:
        rest, digit = divmod(ll1_pointer.value + ll2_pointer.value + rest, 10)
        ll_result.prepend(digit)

        ll1_pointer = ll1_pointer.prev
        ll2_pointer = ll2_pointer.prev

    def fill_remaining_values(pointer, rest):
        while pointer:
            if rest:
                rest, digit = divmod(pointer.value + rest, 10)
                ll_result.prepend(digit)
            else:
                ll_result.prepend(pointer.value)
            pointer = pointer.prev

        if rest:
            ll_result.prepend(rest)

    # If there are still some digits in the ll1 (ll2 is exhausted)
    if ll1_pointer:
        fill_remaining_values(ll1_pointer, rest)
    elif ll2_pointer:
        fill_remaining_values(ll2_pointer, rest)
    elif rest:
        # If there is still some rest (this happens when both pointers were exhausted at the same time)
        ll_result.prepend(rest)

    return ll_result


if __name__ == '__main__':
    # a = 1, 2, 3, 4, 5
    # b = 8, 7, 6, 6, 2
    a = 4, 1
    b = 1, 9
    digits_a = LinkedList(a)
    print(digits_a)
    digits_b = LinkedList(b)
    print(digits_b)
    result = add_numbers(digits_a, digits_b)
    print(result)
    print(f"{get_number(digits_a)} + {get_number(digits_b)} = {get_number(result)}")
