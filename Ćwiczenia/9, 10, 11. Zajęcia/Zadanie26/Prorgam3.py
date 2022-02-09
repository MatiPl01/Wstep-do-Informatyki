# Fully class-based implementation

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


def found_list(ll1_curr, ll2_curr) -> bool:
    # ll2 linked list will never be longer than the ll1 so either both lists are exhausted
    # or the ll2 is exhausted. In both cases we had to iterate over all of the values in the ll2
    # so we are sure that a matching list was found
    while ll2_curr:
        if ll1_curr.value != ll2_curr.value:
            return False
        ll1_curr = ll1_curr.next
        ll2_curr = ll2_curr.next

    return True


def includes_linked_list(ll1: 'an outer linked list', ll2: 'an inner linked list') -> bool:
    if len(ll2) > len(ll1):
        return False

    ll1_ptr = ll1.head
    for _ in range(len(ll1) - len(ll2) + 1):
        if ll1_ptr.value == ll2.head.value and found_list(ll1_ptr.next, ll2.head.next):
            return True

        ll1_ptr = ll1_ptr.next

    return False


if __name__ == '__main__':
    ll1 = LinkedList([*range(2, 10, 3), *(int(d)**3 for d in '937'), *'Python'.partition('t'), True, float('inf')])
    print(ll1)
    ll2 = LinkedList([27, 343, 'Py', 't'])
    print(ll2)

    print(includes_linked_list(ll1, ll2))
