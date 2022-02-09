import random
from functools import wraps


def process_idx(method):
    @wraps(method)
    def inner(instance, idx=None, *args, **kwargs):
        if idx is not None:
            if not isinstance(idx, int):
                raise TypeError(f"Expected 'int', got {str(type(idx))[7:-1]}.")
            if idx < 0:
                idx += instance.length
            if not 0 <= idx < instance.length:
                raise IndexError("Index out of range.")
        return method(instance, idx, *args, **kwargs)
    return inner


def not_empty(method_name):
    def decorator(method):
        @wraps(method)
        def inner(instance, *args, **kwargs):
            if not instance:
                raise IndexError(f"Cannot {method_name} from an empty {instance.__class__.__name__}.")
            return method(instance, *args, **kwargs)
        return inner
    return decorator


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = self.tail = None
        self.length = 0

        self.__initialize(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.initial_value})"

    def __str__(self):
        return ' <-> '.join(str(v) for v in self)

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

    def remove_node(self, node):
        if node is self.tail:
            self.tail = self.tail.prev
            if self.tail:  # If removed non-last element from the doubly linked list
                self.tail.next = None
            else:  # If removed the last element of the list, reset a head pointer
                self.head = None
        elif node is self.head:
            self.head = self.head.next
            if self.head:  # If removed non-last element from the doubly linked list
                self.head.prev = None
            else:  # If removed the first element of the list, reset a tail pointer
                self.tail = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node.value

    @not_empty('pop')
    @process_idx
    def pop(self, idx):
        if idx is None:
            removed_node = self.tail
        elif idx == 0:
            removed_node = self.head
        else:
            center_idx = self.length//2
            removed_node = self.__traverse_from_right(idx) if idx > center_idx else self.__traverse_from_left(idx)
        return self.remove_node(removed_node)

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

    def __traverse_from_left(self, idx):
        curr = self.head
        i = 0
        while idx != i:
            i += 1
            curr = curr.next
        return curr

    def __traverse_from_right(self, idx):
        curr = self.tail
        i = self.length-1
        while idx != i:
            i -= 1
            curr = curr.prev
        return curr


def random_numbers_list(count: int, min_num: int, max_num: int) -> [int]:
    return [random.randint(min_num, max_num) for _ in range(count)]


def count_bin_ones(num: int) -> int:
    count = 0

    while num:
        num, digit = divmod(num, 2)
        count += digit

    return count


def is_odd(num: int) -> bool:
    return num % 2 == 1


def remove_proper_values(dll: DoublyLinkedList):
    while dll and is_odd(count_bin_ones(dll.head.value)):
        dll.pop(0)

    curr = dll.head
    while curr:
        if is_odd(count_bin_ones(curr.value)):
            dll.remove_node(curr)
        curr = curr.next


if __name__ == '__main__':
    random.seed(0)
    # numbers = [50, 2, 1, 4]
    numbers = random_numbers_list(15, 1, 100)
    dll = DoublyLinkedList(numbers)
    print('before:', dll)
    remove_proper_values(dll)
    print('after:', dll)

    def check(lst):
        for n in lst:
            ones = count_bin_ones(n)
            print(n, ones, is_odd(ones), bin(n))
    check(numbers)
