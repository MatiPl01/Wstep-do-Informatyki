"""
Quite good implementation of LinkedList (not functional)
"""

from functools import wraps


def not_empty(method_name):

    def decorator(method):
        @wraps(method)
        def inner(self, *args, **kwargs):
            if not self:
                raise IndexError(f"Cannot {method_name} from empty LinkedList.")
            return method(self, *args, **kwargs)
        return inner

    return decorator


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, values=()):
        self.values_str = ', '.join(str(v) for v in values)

        self.head = self.tail = None
        self.length = 0

        self.extend(values)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.values_str})"

    def __str__(self):
        return ' -> '.join(str(v) for v in self)

    def __len__(self):
        return self.length

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next

    def __getitem__(self, idx):
        idx = self._process_idx(idx)
        return self._get_item(idx).value

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"Can only concatenate LinkedList (not {str(type(other))[7:-1]}) to LinkedList.")
        else:
            new_lst = self.copy()
            new_lst.extend(other)
            return new_lst

    def __mul__(self, num):
        if not isinstance(num, int):
            raise TypeError(f"can't multiply LinkedList by non-int of type {str(type(num))[7:-1]}.")

        new_lst = self.copy()
        for _ in range(num-1):
            new_lst.extend(self)
        return new_lst

    def __rmul__(self, num):
        return self * num

    def append(self, value):
        node = Node(value)
        if not self:
            self.head = self.tail = node
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def prepend(self, value):
        if self:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.length += 1
        else:
            self.append(value)

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    @not_empty('remove')
    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
        else:
            try:
                curr = self.head

                while curr.next.value != value:
                    curr = curr.next

                curr.next = curr.next.next
                self.length -= 1
            except AttributeError:
                raise ValueError(f"Cannot perform .remove({value}). {value} not in LinkedList.")

    @not_empty('pop')
    def pop(self, idx=-1):
        idx = self._process_idx(idx)
        if idx == 0:
            removed = self.head
            self.head = self.head.next
        else:
            prev = self._get_item(idx-1)
            removed = prev.next
            prev.next = prev.next.next

            if idx == self.length-1:
                self.tail = prev

        self.length -= 1
        return removed.value

    def insert(self, idx, value):
        idx = self._process_idx(idx, check_range=False)
        if idx <= 0:
            self.prepend(value)
        elif idx >= self.length:
            self.append(value)
        else:
            prev = self._get_item(idx-1)
            node = Node(value)
            node.next = prev.next
            prev.next = node
            self.length += 1

    def count(self, value):
        total = 0
        for val in self:
            total += val == value
        return total

    def index(self, value):
        for i, val in enumerate(self):
            if val == value:
                return i
        else:
            raise ValueError(f"{value} not in LinkedList.")

    def copy(self):
        return self.__class__(self)

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def reverse(self):
        temp_lst = LinkedList()
        for val in self:
            temp_lst.prepend(val)
        self.head = temp_lst.head
        self.tail = temp_lst.tail

    def _process_idx(self, idx, *, check_range=True):
        if idx < 0:
            idx += self.length
        if check_range and not 0 <= idx < self.length:
            raise IndexError('LinkedList index out of range.')
        return idx

    def _get_item(self, idx):
        curr = self.head
        for _ in range(idx):
            curr = curr.next
        return curr


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 1])
    print(ll)
    print(len(ll))
    print(repr(ll))
    ll.remove(1)
    print(ll)
    ll.remove(1)
    print(ll)
    ll.remove(2)
    print(ll)
    # ll.remove(12)
    ll.remove(3)
    print(ll)
    # ll.remove(12)
    ll.extend([7, 8, 9, 0])
    print(ll)
    print(ll.pop(-3), ll.pop())
    print(ll)
    ll.insert(4141, 1)
    ll.insert(-51341, 1)
    print(ll)
    print(ll.count(1))
    print(9 in ll)

    ll2 = ll.copy()
    ll2.extend([1, 2, 3])
    print(ll, ll2, sep='\t')
    print(ll2 + ll)
    print(5 * ll)
    ll2.clear()
    print(ll2)
    print(ll)
    ll.reverse()
    print(ll)
