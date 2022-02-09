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

    def prepend(self, value):
        node = Node(value)
        if self:
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


def random_numbers_list(count: int, min_num: int, max_num: int) -> [int]:
    return [random.randint(min_num, max_num) for _ in range(count)]


def has_odd_number_of_fives_in_octal_system(num: int) -> bool:
    fives_count = 0

    while num:
        num, dgt = divmod(num, 8)
        if dgt == 5:
            fives_count += 1

    return not fives_count % 2


def move_proper_values(ll: LinkedList):
    # We can omit ll.head no matter which value it has as all matching values will be prepended to the ll
    prev, curr = ll.head, ll.head.next

    while curr:
        value = curr.value
        if has_odd_number_of_fives_in_octal_system(value):
            prev.next = curr.next
            ll.length -= 1  # We have to decrement a length of the linked list because prepend method will increase it
            ll.prepend(value)
            curr = prev.next = curr.next
        else:
            prev, curr = curr, curr.next


if __name__ == '__main__':
    values = random_numbers_list(15, 1, 100)
    ll = LinkedList(values)
    print(ll)
    move_proper_values(ll)
    print(ll)
