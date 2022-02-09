# Class-based implementation

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, length: int):
        if not isinstance(length, int):
            raise TypeError(f"Expected 'int' in {self.__class__.__name__} initialisation, got {str(type(length))[7:-1]}")
        if length < 1:
            raise ValueError(f"Cannot build empty or negative-length {self.__class__.__name__}")

        self.length = length

        # Build empty LinkedList of a specified number of elements
        self.head = Node()

        curr = self.head
        for _ in range(length-1):
            curr.next = Node()
            curr = curr.next

    def __repr__(self):
        return f"{self.__class__.__name__}({self.length})"

    def __str__(self):
        return ' -> '.join(str(v) for v in self)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __getitem__(self, idx):
        self.__check_idx(idx)
        return self.__traverse_to_idx(idx).value

    def __setitem__(self, idx, value):
        self.__check_idx(idx)
        self.__traverse_to_idx(idx).value = value

    def __check_idx(self, idx):
        if not isinstance(idx, int):
            raise TypeError(f"Expected 'int', got {str(type(idx))[7:-1]}")
        if idx >= self.length:
            raise IndexError(f"Index out of range")

    def __traverse_to_idx(self, idx):
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        return curr


if __name__ == '__main__':
    ll = LinkedList(4)
    # LinkedList(0)
    print(ll[3])
    ll[3] = 2
    # ll[4] = 2
    print(repr(ll))
    print(ll)
    ll[1] = -8
    print(ll)
    print(ll[3])
