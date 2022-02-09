class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedDict:
    def __init__(self, value=None):
        self.initial_value = value
        self.head = self.tail = None
        self.length = 0
        self.__initialize(value)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.initial_value})"

    def __str__(self):
        return ' -> '.join(f"{key}: {value}" for key, value in self.items())

    def __iter__(self):
        return self.keys()

    def __len__(self):
        return self.length

    def __setitem__(self, key, value):
        if self:
            item = self.__traverse_to_item(key)
            if item:
                item.value = value
            else:
                node = Node(key, value)
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                self.length += 1
        else:
            node = Node(key, value)
            self.head = self.tail = node
            self.length += 1

    def __getitem__(self, key):
        if self:
            item = self.__traverse_to_item(key)
            if item:
                return item

        raise KeyError(key)

    def __delitem__(self, key):
        self.pop(key)

    def keys(self):
        return LinkedDictKeys(self)

    def values(self):
        return LinkedDictValues(self)

    def items(self):
        return LinkedDictItems(self)

    def pop(self, key):
        if self:
            item = self.__traverse_to_item(key)
            if item:
                value = item.value
                if item.prev and item.next:
                    item.prev.next = item.next
                    item.next.prev = item.prev
                elif item.next:  # item is the first element of the LinkedDict
                    item.next.prev = None
                    self.head = item.next
                else:            # item is the last element of the LinkedDict
                    item.prev.next = None
                    self.tail = item.prev
                self.length -= 1
                return value
        else:
            raise KeyError(key)

    def popitem(self):
        if self:
            key, value = self.tail.key, self.tail.value
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
            return key, value
        raise KeyError(f"popitem(): {self.__class__.__name__} is empty")

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value
        return self[key]

    def update(self, other):
        if isinstance(other, self.__class__) or isinstance(other, dict):
            for key, value in other.items():
                self[key] = value

    @classmethod
    def fromkeys(cls, keys, value=None):
        ld = cls()
        for key in keys:
            ld[key] = value
        return ld

    def __initialize(self, value):
        if isinstance(value, self.__class__) or isinstance(value, dict):
            for key, val in value.items():
                self[key] = val
        elif value is not None:
            raise ValueError(f"Expected '{self.__class__.__name__}' or 'dict', got {str(type(value))[7:-1]}")

    def __traverse_to_item(self, key):
        curr = self.head
        while True:
            if curr.key == key:
                return curr
            elif not curr.next:
                return None
            else:
                curr = curr.next


class LinkedDictKeys:
    def __init__(self, ld: LinkedDict):
        self.ld = ld

    def __repr__(self):
        return f"{self.__class__.__name__}({list(self)})"

    def __iter__(self):
        return self.iterate(lambda curr: curr.key)

    def iterate(self, fn):
        curr = self.ld.head
        while curr:
            yield fn(curr)
            curr = curr.next


class LinkedDictValues(LinkedDictKeys):
    def __iter__(self):
        return self.iterate(lambda curr: curr.value)


class LinkedDictItems(LinkedDictKeys):
    def __iter__(self):
        return self.iterate(lambda curr: (curr.key, curr.value))


if __name__ == '__main__':
    ld = LinkedDict({'a': 1, 'b': 2, 'c': 3})
    print(ld)
    print(ld.items())
    ld['b'] = 4
    ld['d'] = 5
    print(ld)
    del ld['a']
    print(ld)
    print(ld.pop('c'))
    print(ld.popitem())
    print(len(ld))
    print(ld)

    ld2 = LinkedDict.fromkeys('python')
    print(ld2)
    ld2.update(ld)
    print(ld2)
    ld2.update({'p': 1, 'y': 2, 't': 3})
    print(ld2)
