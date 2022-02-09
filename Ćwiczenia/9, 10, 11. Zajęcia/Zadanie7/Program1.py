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


def pop_last_element(first_node: Node) -> 'value of the last node':
    if first_node.value is None:
        raise IndexError("Cannot 'pop' from empty LinkedList")

    if not first_node.next:
        value = first_node.value
        first_node.value = None
    else:
        curr = first_node
        while curr.next.next:
            curr = curr.next
        value = curr.next.value
        curr.next = None
    return value


if __name__ == '__main__':
    ll = LinkedList()
    print(ll)
    append_to_linked_list(ll.head, 1)
    append_to_linked_list(ll.head, 2)
    append_to_linked_list(ll.head, 3)
    append_to_linked_list(ll.head, 4)
    print(ll)
    print(pop_last_element(ll.head))
    print(ll)
    print(pop_last_element(ll.head))
    print(pop_last_element(ll.head))
    print(pop_last_element(ll.head))
    print(ll)
    # print(pop_last_element(ll.head))

    # Append to show that after last pop linked list remains empty
    append_to_linked_list(ll.head, 123)
    print(ll)
