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


def remove_longest_increasing_sublist(ll: LinkedList):
    prev, curr = ll.head, ll.head.next
    max_length = curr_length = 1
    to_remove_begin_prev = to_remove_begin_prev_curr = None
    to_remove_end_next = None
    more_than_one_sequence = False

    # Find a node previous to the beginning of the longest increasing subsequence and a node next to the last one
    while curr:
        if curr.next and curr.next.value > prev.next.value:
            curr_length += 1
            if prev is ll.head:
                curr_length += 1
                to_remove_begin_prev_curr = None
            elif curr_length == 2:
                to_remove_begin_prev_curr = prev

        else:  # Else block will be executed either if we leave an increasing sublist or if a linked list is exhausted
            if curr_length > max_length:
                max_length = curr_length
                to_remove_begin_prev = to_remove_begin_prev_curr
                to_remove_end_next = curr.next
                more_than_one_sequence = False
            elif curr_length == max_length:
                to_remove_begin_prev = None
                more_than_one_sequence = True

            to_remove_begin_prev_curr = None
            curr_length = 1

        prev, curr = curr, curr.next

    # Remove appropriate values
    if not more_than_one_sequence:
        if to_remove_begin_prev:
            to_remove_begin_prev.next = to_remove_end_next
            ll.length -= max_length
        elif to_remove_end_next:
            ll.head = to_remove_end_next
            ll.length -= max_length


if __name__ == '__main__':
    # values = 1, 2, 3, 4, 2, 8, 1, 0, -5, -12, -3, -1, 2, 5, 0
    # values = 1, 2, 3, 4, 2, 8, 1, 0, -5, -12, -3, -1, 2, 5, 8, 10
    values = 1, 2, 3, 4, 2, 8, 1, 0, 2, 3, 4, 5, -5, -12, -3, -1
    ll = LinkedList(values)
    print(ll)
    print(len(ll))
    remove_longest_increasing_sublist(ll)
    print(ll)
    print(len(ll))
