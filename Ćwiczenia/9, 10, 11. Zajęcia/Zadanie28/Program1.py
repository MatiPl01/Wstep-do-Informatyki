import random
from functools import wraps


def not_empty(method_name):
    def decorator(method):
        @wraps(method)
        def inner(instance, *args, **kwargs):
            print(bool(instance), instance.length)
            if not instance:
                raise IndexError(f"Cannot {method_name} from an empty {instance.__class__.__name__}.")
            return method(instance, *args, **kwargs)
        return inner
    return decorator


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

    @not_empty('remove')
    def remove(self, value, *, iterate_while=lambda curr, passed: curr != passed):
        self.prepend(None)  # Create a sentinel node to ease operations
        curr = self.head
        while curr.next and iterate_while(curr.next.value, value):
            curr = curr.next
            # print(curr.value)

        if curr.next and curr.next.value == value:
            curr.next = curr.next.next
            self.head = self.head.next  # Remove a sentinel node
        else:
            self.head = self.head.next  # Remove a sentinel node
            raise ValueError(f"{self.__class__.__name__}.remove(value): value not in {self.__class__.__name__}")
        self.length -= 2  # We subtract 2 as we remove a sentinel node and the value passed

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


def get_sorted_random_int_list(length: int, min_num: int, max_num: int) -> [int]:
    return sorted(random.randint(min_num, max_num) for _ in range(length))


def remove_common_values(ll1: LinkedList, ll2: LinkedList):
    ll2.prepend(None)  # Create a sentinel node to ease operations

    curr = ll2.head
    while curr.next:
        try:
            # Thanks to the callback function we make use of the fact that values of the ll1 linked list are sorted
            # in an increasing order. This function allows us to stop searching for a value to remove just after
            # having encountered a value that is greater than the searched one.
            ll1.remove(curr.next.value, iterate_while=lambda curr, passed: curr < passed)
        except ValueError:
            # Move ahead the pointer of the ll2 if an error was raised (that means ll1 doesn't have curr.value value).
            curr = curr.next
        else:
            # If there had been no error raised while trying to remove a value from the ll1 linked list, we are sure
            # that both ll1 and ll2 have this value in common. Hence, we can remove this value from ll2.
            curr.next = curr.next.next
            ll2.length -= 1

    # Remove a sentinel node created before
    ll2.head = ll2.head.next
    ll2.length -= 1


if __name__ == '__main__':
    random.seed(0)
    ll1_items = sorted(set(get_sorted_random_int_list(10, 0, 20)))
    ll2_items = set(get_sorted_random_int_list(6, 5, 15))

    # ll2_items = [1, 8, 9, 11, 12, 13, 15, 16]
    # ll1 = LinkedList(ll1_items)
    # ll2 = LinkedList(ll2_items)
    # print('Before:', ll1, ll2, sep='\n', end='\n\n')
    # remove_common_values(ll1, ll2)
    # print('After:', ll1, ll2, sep='\n', end='\n\n')

    ll = LinkedList([1, 2, 3])
    print(ll)
    ll.remove(1)
    ll.remove(2)
    ll.remove(3)
    print(ll)
    ll.remove(1)
    print(ll)
