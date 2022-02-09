from functools import reduce


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_sorted_linked_list(values):
    values = sorted(values)
    values_iterator = iter(values)
    head = Node(next(values_iterator))
    curr = head
    for value in values_iterator:
        curr.next = Node(value)
        curr = curr.next
    return head


def print_linked_list(first_node):
    curr_node = first_node
    print(curr_node.val, end=' ')
    while curr_node.next:
        curr_node = curr_node.next
        print('->', curr_node.val, end=' ')
    print()


def pop_first(first_node):
    if not first_node.next:
        return None

    removed_val = first_node.val
    first_node.val = first_node.next.val
    first_node.next = first_node.next.next
    return removed_val


def get_lowest_val_node(nodes):
    return reduce(lambda l_val, curr: l_val if l_val.val < curr.val else curr, nodes)


def union(*linked_sets):
    linked_sets = set(linked_sets)
    first_node = get_lowest_val_node(linked_sets)
    linked_sets.remove(first_node)
    curr_node = first_node.next

    while linked_sets:
        next_node = get_lowest_val_node(linked_sets)
        # print_linked_list(first_node)
        # print('next', next_node.val)
        # print('curr', curr_node.val)

        # Go to the last lowest value node of the current linked list
        while curr_node.next and curr_node.next.val < next_node.val:
            curr_node = curr_node.next

        # Remove linked list that we linked to the current one in order not to check the same values again
        linked_sets.remove(next_node)

        # If the next_node value is equal to the current one and there are still some values after next_node in the list
        if curr_node.next and next_node.val == curr_node.next.val and next_node.next:
            linked_sets.add(next_node.next)
        else:
            # Store nodes that we unplug from the current linked list
            remaining_nodes = curr_node.next
            if remaining_nodes:
                linked_sets.add(remaining_nodes)
            curr_node.next = next_node

    # print('STORED')
    # [print_linked_list(ll) for ll in linked_sets]
    # print('END')

    return first_node


if __name__ == '__main__':
    values1 = {4, 1, 6, 12, 7}
    values2 = {25, 6, 11, 16, 16, 14, 22}
    values3 = {15, 28, 54, 41, 21, 23}
    z1 = create_sorted_linked_list(values1)
    z2 = create_sorted_linked_list(values2)
    z3 = create_sorted_linked_list(values3)
    print_linked_list(z1)
    print_linked_list(z2)
    print_linked_list(z3)
    result = union(z1, z2, z3)
    print_linked_list(result)
