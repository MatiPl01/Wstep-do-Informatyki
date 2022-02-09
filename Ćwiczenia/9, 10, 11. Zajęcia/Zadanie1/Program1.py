from functools import wraps


def is_natural(fn):

    @wraps(fn)
    def inner(instance, num):
        if not isinstance(num, int):
            raise ValueError(f"Expected a natural number, got {str(type(num))[7:-1]}.")
        if num < 0:
            raise ValueError(f"Expected a natural number, got a negative integer.")
        return fn(instance, num)

    return inner


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class NaturalNumbers:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return ' -> '.join(str(v) for v in self)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __len__(self):
        return self.length

    def __contains__(self, value):
        # I implement my own 'in' inclusion checking method to be sure that value is
        # a natural number. Floats of the same value will be treated as different numbers.
        if isinstance(value, int) and value >= 0:
            for val in self:
                if val == value:
                    return True
        return False

    @is_natural
    def add(self, value):
        node = Node(value)
        if self:
            if self.tail.value < value:
                self.tail.next = node
                self.tail = node
                self.length += 1
            else:
                prev_node = self.__get_lower_value_node(value)
                if prev_node.next.value != value:
                    node.next = prev_node.next
                    prev_node.next = node
                    self.length += 1
        else:
            self.tail = self.head = node
            self.length += 1

    @is_natural
    def remove(self, value):
        if not self:
            raise ValueError('Cannot remove a number from an empty set of natural numbers.')

        if self.tail.value < value:
            raise ValueError(f"Cannot remove a number from a set of natural numbers. {value} not in set.")

        if self.head.value == value:
            self.head = self.head.next
        else:
            prev_node = self.__get_lower_value_node(value)
            if prev_node.next.value == value:
                prev_node.next = prev_node.next.next

        self.length -= 1

    def __get_lower_value_node(self, value):
        return self.__traverse_while(lambda curr, passed: curr.value < passed, value)

    def __traverse_while(self, fn, *args, **kwargs):
        curr = self.head
        while fn(curr.next, *args, **kwargs):
            curr = curr.next
        return curr


if __name__ == '__main__':
    naturals = NaturalNumbers()
    naturals.add(1)
    naturals.add(2)
    naturals.add(5)
    naturals.add(4)
    naturals.add(3)
    print(3.0 in naturals)
    print(naturals)
    naturals.remove(5)
    naturals.remove(1)
    naturals.remove(3)
    print(naturals)
    naturals.add(3)
    naturals.add(3)
    naturals.add(3)
    print(naturals)
    print(len(naturals))
    naturals.remove(2)
    naturals.remove(3)
    naturals.remove(4)
    print(naturals, len(naturals))
    naturals.add(15)
    print(naturals)
