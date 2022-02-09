class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class WordsCycle:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = None
        self.length = 0

        self.__initialize(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.initial_value})"

    def __str__(self):
        if self:
            values = [str(self.head.value)]
            curr = self.head.next
            while curr is not self.head:
                values.append(str(curr.value))
                curr = curr.next
            return f"({' -> '.join(values)})"
        else:
            return ''

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self.length

    def add_entry(self, value):
        self.check_if_string(value)
        node = Node(value)
        try:
            if self:
                prev = self.traverse_while(value, lambda prev, curr, passed: not self.is_preceding(prev, curr, passed))
                node.next = prev.next
                prev.next = node
            else:
                self.head = node
                self.head.next = node
        except StopIteration:
            return False
        else:
            self.head = node
            self.length += 1
            return True

    def add_entries(self, iterable):
        self.check_if_strings_iterable(iterable)
        added = True
        for value in iterable:
            added = self.add_entry(value) and added
        return added

    def traverse_while(self, value, fn):
        curr = self.head
        while fn(curr.value, curr.next.value, value):
            curr = curr.next
            if curr is self.head:
                raise StopIteration()
        return curr

    def __initialize(self, value):
        if value is None:
            value = []
        self.add_entries(value)

    @staticmethod
    def check_if_string(value):
        if not isinstance(value, str):
            raise TypeError

    @staticmethod
    def check_if_strings_iterable(value):
        if not (hasattr(value, '__iter__') and all(isinstance(v, str) for v in value)):
            raise TypeError("Expected an iterable of strings.")

    @staticmethod
    def is_preceding(prev, curr, passed):
        return passed[-1] < curr[0] and prev[-1] < passed[0]


if __name__ == '__main__':
    wc = WordsCycle(['bartek', 'ola'])
    print(wc)
    print(wc.add_entry('leszek'))
    print(wc)
    print(wc.add_entries({'zosia', 'marek'}))  # Because of this set in here we can get different results
    print(wc)                                  # (Run code a few times to see results)
    print(wc.add_entry('leszek'))
    print(wc)
    print(wc.add_entry('karol'))
    print(wc)
    print(len(wc))

    # for v in ll:
    #     print(v)
