import random


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_cycle(values):
    # Create a linked list
    values_iterator = iter(values)
    first_node = Node(next(values_iterator))
    curr = first_node
    for value in values_iterator:
        curr.next = Node(value)
        curr = curr.next
    # Join the last node to the first one
    curr.next = first_node
    return first_node


def print_cycle(begin_ptr):
    curr = begin_ptr
    print('(', curr.val, end=' ')
    while curr.next is not begin_ptr:
        curr = curr.next
        print('->', curr.val, end=' ')
    print(')')


def get_random_ll_ptr(first_node, length):
    curr = first_node
    for _ in range(random.randint(0, length-1)):
        curr = curr.next
    return curr


def random_list(length: int, min_num: int, max_num: int) -> [int]:
    return [random.randint(min_num, max_num) for _ in range(length)]


def remove_node(cycle, node):
    if node is node.next:
        raise KeyError('Cannot remove the last one node from a cycle.')

    node.val = node.next.val
    if node.next is cycle:  # We cannot omit the first node
        first_node = node.next
        first_node.val = first_node.next.val
        first_node.next = first_node.next.next
    else:
        node.next = node.next.next


def get_lowest_val_ptr(cycle):
    # Move pointer of the cycle to the lowest value
    cycle_begin_ptr = cycle
    cycle_curr = cycle.next

    while cycle_curr is not cycle:
        if cycle_curr.val < cycle_begin_ptr.val:
            cycle_begin_ptr = cycle_curr
        cycle_curr = cycle_curr.next

    return cycle_begin_ptr


def remove_common_values(ll1, ll2):
    ll1_curr = get_lowest_val_ptr(ll1)
    ll2_begin_ptr = get_lowest_val_ptr(ll2)

    # Iterate through ll1
    while True:
        # Iterate through ll2 and look for values to remove
        ll2_curr = ll2_begin_ptr
        while ll2_curr.val < ll1_curr.val:
            ll2_curr = ll2_curr.next

        # Remove values from both lists if are equal
        if ll2_curr.val == ll1_curr.val:
            remove_node(ll1, ll1_curr)
            remove_node(ll2, ll2_curr)
        else:
            ll1_curr = ll1_curr.next
        if ll1_curr is ll1:
            break


if __name__ == '__main__':
    length1 = 15
    length2 = 15
    random.seed(5)
    ll1 = create_cycle(sorted(random_list(5, 1, length1)))
    ll2 = create_cycle(sorted(random_list(7, 5, length2)))
    print_cycle(ll1)
    print_cycle(ll2)
    ptr1 = get_random_ll_ptr(ll1, length1)
    ptr2 = get_random_ll_ptr(ll2, length2)
    remove_common_values(ptr1, ptr2)
    print_cycle(ptr1)
    print_cycle(ptr2)
