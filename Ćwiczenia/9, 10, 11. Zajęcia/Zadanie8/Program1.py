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


def remove_every_other_item(ll: LinkedList, *, start_with_first=False):
    curr = ll.head

    if not curr or not curr.next:
        raise ValueError('Cannot remove values of linked list of length lower than 2')

    i = 0
    if start_with_first:
        curr.value = curr.next.value
        curr.next = curr.next.next
        ll.length -= 1

    while curr.next:
        if not i % 2:  # i is divisible by 2
            curr.next = curr.next.next
            ll.length -= 1
        else:
            curr = curr.next
        i += 1


if __name__ == '__main__':
    ll = LinkedList(random_numbers_list(2, 0, 100))
    print(ll)
    remove_every_other_item(ll, start_with_first=True)
    print(ll)

    ll = LinkedList(random_numbers_list(2, 0, 100))
    print(ll)
    remove_every_other_item(ll)
    print(ll)

    ll = LinkedList(random_numbers_list(15, 0, 100))
    print(ll)
    remove_every_other_item(ll, start_with_first=True)
    print(ll)
    print(len(ll))

    ll = LinkedList(random_numbers_list(15, 0, 100))
    print(ll)
    remove_every_other_item(ll)
    print(ll)
    print(len(ll))
