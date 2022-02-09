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


def create_cycle(ll: LinkedList, idx: 'an index of the first element of a cycle'):
    if idx >= len(ll):
        raise IndexError("Cannot create a cycle, index out of range.")

    curr = ll.head
    for _ in range(idx):
        curr = curr.next

    ll.tail.next = curr


def cycle_length(ll: LinkedList) -> int:
    if not ll.tail.next:
        return 0

    curr = ll.tail.next
    count = 1
    while curr is not ll.tail:
        curr = curr.next
        count += 1

    return count


def get_cycle_values(ll: LinkedList) -> list:
    if not ll.tail.next:
        return []

    result = []
    curr = ll.tail.next
    while curr is not ll.tail:
        result.append(curr.value)
        curr = curr.next
    result.append(curr.value)

    return result


if __name__ == '__main__':
    values = random_numbers_list(10, 0, 100)
    ll = LinkedList(values)
    print(ll)
    create_cycle(ll, 7)
    print(cycle_length(ll))
    print(get_cycle_values(ll))
