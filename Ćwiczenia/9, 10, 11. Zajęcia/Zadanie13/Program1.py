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


def remove_proper_values(ll: LinkedList):
    prev = ll.head
    curr = prev.next
    to_remove_begin = None
    removed_length = 0

    while curr:
        if curr.value < prev.value:
            removed_length += 1
            if not to_remove_begin:
                to_remove_begin = prev
        elif to_remove_begin:
            to_remove_begin.next = curr
            ll.length -= removed_length
            removed_length = 0
            to_remove_begin = None

        prev, curr = curr, curr.next


if __name__ == '__main__':
    numbers = random_numbers_list(15, 0, 100)
    numbers[5:12] = sorted(numbers[5:12], reverse=True)
    ll = LinkedList(numbers)
    print(ll)
    remove_proper_values(ll)
    print(ll)
    print(len(ll))
