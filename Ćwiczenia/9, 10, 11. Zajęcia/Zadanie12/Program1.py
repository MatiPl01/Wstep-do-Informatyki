class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedDictionary:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = self.tail = None
        self.length = 0

        self.__initialize(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.initial_value})"

    def __str__(self):
        return ' -> '.join(v for v in self)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self.length

    def add_entry(self, entry: str) -> bool:
        if not isinstance(entry, str):
            raise TypeError(f"Expected 'str', got {str(type(entry))[7:-1]}")

        entry = entry.lower()
        if not self:
            self.head = self.tail = Node(entry)
        elif entry > self.tail.value:
            self.tail.next = Node(entry)
            self.tail = self.tail.next
        elif entry < self.head.value:
            node = Node(entry)
            node.next = self.head
            self.head = node
        elif entry == self.head.value or entry == self.tail.value:
            return False
        else:
            prev_node = self.traverse_while(lambda curr, passed: passed > curr, entry)

            # If the node at which we stopped has the same value as the entry variable, return False
            if prev_node.next.value == entry:
                return False

            node = Node(entry)
            node.next = prev_node.next
            prev_node.next = node

        self.length += 1
        return True

    def add_entries(self, entries: 'an iterable of strings') -> bool:
        all_added = True
        for entry in entries:
            not_in_dictionary = self.add_entry(entry)
            all_added = all_added and not_in_dictionary
        return all_added

    def traverse_while(self, fn, *args, **kwargs):
        curr = self.head
        while curr and fn(curr.next.value, *args, **kwargs):
            curr = curr.next
        return curr

    def __initialize(self, value):
        if value is None:
            value = 0
        if isinstance(value, int):
            if value >= 0:
                for _ in range(value):
                    self.add_entry('')
            else:
                raise ValueError(f"Expected a positive integer, got {value}.")
        elif hasattr(value, '__iter__'):
            self.add_entries(value)
        else:
            raise TypeError(f"Expected an iterable or 'int', got {str(type(value))[7:-1]}.")


if __name__ == '__main__':
    ld = LinkedDictionary(['Python', 'programming', 'linked', 'dictionary'])
    print(ld)
    print(ld.add_entries('Something NEW is being ADDED to the dictionary'.split()))
    print(ld)
    print(ld.add_entry('test'))
    print(ld)
    print(ld.add_entries('Something NEW is being added to the dictionary'.swapcase().split()))
    print(ld)
    # ld.add_entry(123)
