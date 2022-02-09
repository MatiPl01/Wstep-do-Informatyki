# Improved bidirectional item insertion
from functools import wraps
# import sys
#
# sys.intern('LEFT')
# sys.intern('RIGHT')


def traverse_function(method):
    functions_dict = {
        'IS_LOWER': lambda passed, curr: passed < curr.value,
        'IS_GREATER': lambda passed, curr: passed > curr.value,
        # 'NOT_LOWER': lambda passed, curr: passed >= curr.value,
        # 'NOT_GREATER': lambda passed, curr: passed <= curr.value,
        # 'NOT_EQUAL': lambda passed, curr: passed != curr.value,
        # 'IS_LONGER': lambda passed, curr: len(passed) > len(curr.value),
        # 'IS_SHORTER': lambda passed, curr: len(passed) < len(curr.value),
    }

    @wraps(method)
    def inner(instance, fn, *args, **kwargs):
        if callable(fn):
            return method(instance, fn, *args, **kwargs)
        if isinstance(fn, str):
            if fn in functions_dict:
                return method(instance, functions_dict[fn], *args, **kwargs)
            else:
                raise ValueError(f"Not valid string passed. No function for '{fn}' was defined.")
        else:
            raise TypeError(f"Expected 'callable' or an appropriate 'string', got {str(type(fn))[7:-1]}.")

    return inner


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedDictionary:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = self.tail = None
        self.length = 0

        self._begin_char_ord_sum = 0
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

        entry = entry
        if not self:
            self.head = self.tail = Node(entry)
        elif entry > self.tail.value:
            node = Node(entry)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        elif entry < self.head.value:
            node = Node(entry)
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            # Traverse from left to right if it's more likely for the current entry to be inserted before the middle
            if self.__is_lower_than_mean(entry):
                fn_name, direction = 'IS_GREATER', 'RIGHT'
            else:
                fn_name, direction = 'IS_LOWER', 'LEFT'

            # If the entry passed already exist in a dictionary, return False
            last_checked = self.traverse_while(fn_name, entry, direction=direction)
            if last_checked.value == entry:
                return False

            # Decide which node should be previous to the current one.
            prev_node = last_checked if direction is 'LEFT' else last_checked.prev

            # Insert a new entry
            node = Node(entry)
            node.next = prev_node.next
            prev_node.next.prev = node
            node.prev = prev_node
            prev_node.next = node

        self.length += 1
        self._begin_char_ord_sum += ord(entry[0])
        return True

    def add_entries(self, entries: 'an iterable of strings') -> bool:
        all_added = True
        for entry in entries:
            not_in_dictionary = self.add_entry(entry)
            all_added = all_added and not_in_dictionary
        return all_added

    @traverse_function
    def traverse_while(self, fn, entry, direction='RIGHT', args=(), kwargs={}):
        if direction is 'RIGHT':
            curr = self.head
            while curr and fn(entry, curr, *args, **kwargs):
                curr = curr.next
        elif direction is 'LEFT':
            curr = self.tail
            while curr and fn(entry, curr, *args, **kwargs):
                curr = curr.prev
        else:
            raise ValueError(f"Expected 'LEFT' or 'RIGHT' as direction value, got '{direction}'.")
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

    def __is_lower_than_mean(self, entry):
        return ord(entry[0]) * self.length < self._begin_char_ord_sum


if __name__ == '__main__':
    dld = DoublyLinkedDictionary(['Python', 'programming', 'linked', 'dictionary'])
    # print(dld)
    print(dld.add_entries('Something NEW is being ADDED to the dictionary'.split()))
    print(dld)
    print(dld.add_entry('test'))
    print(dld.add_entry('new'))
    print(dld.add_entry('NEW'))
    print(dld)
    # dld.add_entry(123)
