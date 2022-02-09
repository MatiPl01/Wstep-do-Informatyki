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


def remove_duplicates(ll: LinkedList):
    all_values = set()
    to_remove = set()

    # Store information about duplicates to remove
    for value in ll:
        if value in all_values:
            to_remove.add(value)
        all_values.add(value)

    # Remove duplicates
    while ll and ll.head.value in to_remove:
        ll.head = ll.head.next
        ll.length -= 1

    prev, curr = ll.head, ll.head.next
    while curr:
        if curr.value in to_remove:  # Checking if a value is in a set is O(1)
            prev.next = curr.next
            curr = curr.next
            ll.length -= 1
        else:
            prev, curr = curr, curr.next


if __name__ == '__main__':
    random.seed(0)
    numbers = random_numbers_list(15, 0, 20)
    ll = LinkedList(numbers)
    print(ll)
    remove_duplicates(ll)
    print(ll)
