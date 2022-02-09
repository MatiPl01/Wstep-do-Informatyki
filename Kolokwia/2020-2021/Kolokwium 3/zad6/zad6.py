"""
Mateusz Łopaciński

Funkcja iloczyn(z1, z2, z3) "rozpakowuje" kolejne wartości ze wszystkich zbiorów, reprezentowanych
przez listy odsyłaczowe, do zbioru values_set. Następnie, przy pomocy zaimplementowanej funkcji
create_sorted_linked_list, tworzona jest nowa lista wynikowa, reprezentująca docelowy zbiór.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iloczyn(z1, z2, z3):
    values_set = set()

    def unpack_values(ptr):
        while ptr:
            values_set.add(ptr.val)
            ptr = ptr.next

    unpack_values(z1)
    unpack_values(z2)
    unpack_values(z3)

    return create_sorted_linked_list(values_set)


# Uznaję, że normalnie posortowane listy są dane
def create_sorted_linked_list(values):
    values = sorted(values)
    values_iterator = iter(values)
    head = Node(next(values_iterator))
    curr = head
    for value in values_iterator:
        curr.next = Node(value)
        curr = curr.next
    return head


# def print_linked_list(first_node):
#     curr_node = first_node
#     print(curr_node.val, end=' ')
#     while curr_node.next:
#         curr_node = curr_node.next
#         print('->', curr_node.val, end=' ')
#     print()


if __name__ == '__main__':
    values1 = {4, 1, 6, 12, 7}
    values2 = {25, 6, 11, 16, 16, 14, 22}
    values3 = {15, 28, 54, 41, 21, 23}
    z1 = create_sorted_linked_list(values1)
    z2 = create_sorted_linked_list(values2)
    z3 = create_sorted_linked_list(values3)
    result = iloczyn(z1, z2, z3)
    # print_linked_list(result)
