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


def have_common_part(range1: list, range2: list) -> bool:
    return range1[0] <= range2[1] and range1[1] >= range2[0]


def get_merged_range(range1: list, range2: list) -> [int, int]:
    return [min(range1[0], range2[0]), max(range1[1], range2[1])]


def reduce_ranges(ll: LinkedList):
    pt1 = ll.head

    while pt1:
        pt2 = pt1
        while pt2.next:   # Iterate over remaining elements
            if have_common_part(pt1.value, pt2.next.value):
                # print(f"{pt1.value} u {pt2.next.value} -> {get_merged_range(pt1.value, pt2.next.value)}")

                # Merge ranges by updating the value of the pt1 node
                pt1.value = get_merged_range(pt1.value, pt2.next.value)
                # Remove pt2 node as we don't need this range anymore
                pt2.next = pt2.next.next
                ll.length -= 1
            else:
                pt2 = pt2.next
        pt1 = pt1.next


if __name__ == '__main__':
    # ranges = [15, 19], [2, 5], [7, 11], [8, 12], [5, 6], [13, 17]
    ranges = [15, 19], [0, 15], [-7, 11], [20, 25], [23, 24], [25, 35]
    ll = LinkedList(ranges)
    print(ll)
    reduce_ranges(ll)
    print(ll)
