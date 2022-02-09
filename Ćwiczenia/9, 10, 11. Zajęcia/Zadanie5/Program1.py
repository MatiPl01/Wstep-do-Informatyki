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
            raise ValueError(f"Expected an iterable or 'int', got {str(type(value))[7:-1]}.")


def random_numbers_list(count: int, min_num: int, max_num: int) -> [int]:
    return [random.randint(min_num, max_num) for _ in range(count)]


def last_digit(num: int) -> int:
    return num % 10


def split_to_10_linked_lists(ll: LinkedList) -> [LinkedList]:
    result = [LinkedList() for _ in range(10)]

    for value in ll:
        result[last_digit(value)].append(value)

    return result


def merge_linked_lists(ll_iterable: 'an iterable of linked lists') -> LinkedList:
    ll_result = LinkedList()

    for ll in ll_iterable:
        # ll_result.extend(ll)

        # For cases when values with the same last digit should be also sorted in non-decreasing orger
        ll_result.extend(sorted(ll))

    return ll_result


if __name__ == '__main__':
    values = random_numbers_list(20, 0, 100)
    ll = LinkedList(values)
    print(ll)
    ll_lst = split_to_10_linked_lists(ll)
    print('\n--- After splitting ---')
    print(*ll_lst, sep='\n', end='\n\n')
    print(merge_linked_lists(ll_lst))
