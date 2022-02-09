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


def split_to_two_proper_lists(ll1: LinkedList, ll2: LinkedList) -> int:
    count = 0

    # Create a sentinel node to ease operations
    ll1.prepend(None)

    # Iterate over elements of ll1 linked list
    curr = ll1.head
    while curr.next:
        if curr.next.value > 0 and not curr.next.value % 2:
            curr = curr.next             # Leave this value in the ll1 linked list
        elif curr.next.value < 0 and curr.next.value % 2:
            ll2.append(curr.next.value)  # Move value to the ll2 linked list
            curr.next = curr.next.next   # Remove a moved value from the ll1 linked list
            ll1.length -= 1
        else:
            curr.next = curr.next.next   # Remove value that doesn't match
            ll1.length -= 1
            count += 1

    # Remove a sentinel node
    ll1.head = ll1.head.next
    ll1.length -= 1

    return count


if __name__ == '__main__':
    values = random_numbers_list(15, -50, 50)
    ll1 = LinkedList(values)
    ll2 = LinkedList()
    print('Before:', ll1, ll2, sep='\n')
    print("Removed count:", split_to_two_proper_lists(ll1, ll2))
    print('After:', ll1, ll2, sep='\n')
