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


def get_sorted_random_int_list(length: int, min_num: int, max_num: int) -> [int]:
    return sorted(random.randint(min_num, max_num) for _ in range(length))


def merge_sorted_linked_lists_iter(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    ll1_iterator = iter(ll1)
    ll2_iterator = iter(ll2)
    ll1_value = next(ll1_iterator)
    ll2_value = next(ll2_iterator)
    ll_merged = LinkedList()

    while True:
        try:
            if ll1_value <= ll2_value:
                ll_merged.append(ll1_value)
                ll1_value = next(ll1_iterator)
            else:
                ll_merged.append(ll2_value)
                ll2_value = next(ll2_iterator)
        except StopIteration:
            break

    # We have to add the last value of the linked list that has been exhausted
    if ll1_value == ll_merged.tail:  # That means ll1 linked list has been exhausted
        ll_merged.append(ll2_value)
        ll_merged.extend(ll2_iterator)
    else:                            # Otherwise, ll2 linked list has been exhausted
        ll_merged.append(ll1_value)
        ll_merged.extend(ll1_iterator)

    return ll_merged


def merge_sorted_linked_lists_recur(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    ll_merged = LinkedList()

    def recur(ll1_pointer=ll1.head, ll2_pointer=ll2.head):
        if ll1_pointer and ll2_pointer:
            if ll1_pointer.value <= ll2_pointer.value:
                ll_merged.append(ll1_pointer.value)
                recur(ll1_pointer.next, ll2_pointer)
            else:
                ll_merged.append(ll2_pointer.value)
                recur(ll1_pointer, ll2_pointer.next)
        elif ll1_pointer:
            ll_merged.append(ll1_pointer.value)
            recur(ll1_pointer.next, ll2_pointer)
        elif ll2_pointer:
            ll_merged.append(ll2_pointer.value)
            recur(ll1_pointer, ll2_pointer.next)

    recur()

    return ll_merged


if __name__ == '__main__':
    ll1_items = get_sorted_random_int_list(10, 0, 100)
    ll2_items = get_sorted_random_int_list(6, 5, 40)
    ll1 = LinkedList(ll1_items)
    ll2 = LinkedList(ll2_items)
    print(ll1, ll2, sep='\n', end='\n\n')
    print(merge_sorted_linked_lists_iter(ll1, ll2))
    print(merge_sorted_linked_lists_recur(ll1, ll2))
