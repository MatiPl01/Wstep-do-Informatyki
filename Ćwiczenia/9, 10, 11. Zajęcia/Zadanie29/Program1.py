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


def get_sorted_random_int_list(length: int, min_num: int, max_num: int) -> [int]:
    return sorted(random.randint(min_num, max_num) for _ in range(length))


def remove_not_common_values(ll1: LinkedList, ll2: LinkedList):
    # Create sentinel nodes to ease operations
    ll1.prepend(None)
    ll2.prepend(None)

    # Iterate over subsequent elements of linked lists
    ll1_ptr = ll1.head
    ll2_ptr = ll2.head

    # While both lists are not yet exhausted.
    iterations = 0  # Store a number of iterations to subtract a proper value from a length of the remaining part
    while ll1_ptr.next and ll2_ptr.next:
        if ll1_ptr.next.value < ll2_ptr.next.value:    # Move ahead the pointer and remove subsequent values of ll1
            ll1_ptr.next = ll1_ptr.next.next
            ll1.length -= 1
        elif ll1_ptr.next.value > ll2_ptr.next.value:  # Move ahead the pointer and remove subsequent values of ll2
            ll2_ptr.next = ll2_ptr.next.next
            ll2.length -= 1
        else:                                          # Skip values if are equal
            ll1_ptr = ll1_ptr.next
            ll2_ptr = ll2_ptr.next

    # The remaining part (is exists) of one of the linked lists won't be common with the other linked list, therefore,
    # it should be removed
    if ll1_ptr.next:
        ll1.length = ll2.length  # Final linked lists will always have the same number of elements
        ll1_ptr.next = None
    elif ll2_ptr.next:
        ll2.length = ll1.length
        ll2_ptr.next = None

    # Remove sentinel nodes
    ll1.head = ll1.head.next
    ll1.length -= 1
    ll2.head = ll2.head.next
    ll2.length -= 1


# def remove_not_common_values(ll1: LinkedList, ll2: LinkedList):
#     final_values = sorted(set(ll1).intersection(ll2))  # Values should remain in an increasing order
#
#     def update_linked_list(ll):
#         new_ll = LinkedList(final_values)
#         ll.head = new_ll.head
#         ll.tail = new_ll.tail
#         ll.length = new_ll.length
#
#     update_linked_list(ll1)
#     update_linked_list(ll2)


if __name__ == '__main__':
    # random.seed(0)
    ll1_items = sorted(set(get_sorted_random_int_list(15, 0, 20)))
    ll2_items = set(get_sorted_random_int_list(10, 5, 15))

    # ll2_items = [1, 8, 9, 11, 12, 13, 15, 16]
    ll1 = LinkedList(ll1_items)
    ll2 = LinkedList(ll2_items)
    print('Before:', ll1, ll2, sep='\n', end='\n\n')
    remove_not_common_values(ll1, ll2)
    print('After:', ll1, ll2, sep='\n', end='\n\n')

    print(len(ll1), len(ll2))
    print(set(ll1).intersection(ll2))
