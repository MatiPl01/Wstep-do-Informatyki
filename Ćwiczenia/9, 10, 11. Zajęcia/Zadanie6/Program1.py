class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return ' -> '.join(str(v) for v in self)

    def __iter__(self):
        if self.head.value is not None:
            curr = self.head
            while curr:
                yield curr.value
                curr = curr.next


def append_to_linked_list(first_node: Node, value):
    if first_node.value is None:
        first_node.value = value
    else:
        curr = first_node
        while curr.next:
            curr = curr.next
        curr.next = Node(value)


if __name__ == '__main__':
    ll = LinkedList()
    print(ll)
    append_to_linked_list(ll.head, 1)
    append_to_linked_list(ll.head, 2)
    append_to_linked_list(ll.head, 3)
    append_to_linked_list(ll.head, 4)
    print(ll)
