# Functions-based implementation
# I assume that we cannot set indices to subsequent nodes

import random

"""
**************************
Linked list implementation
**************************
"""

create_node = lambda value=0: {'value': value, 'next': None}


def create_linked_list(length: int) -> dict:
    if not isinstance(length, int):
        raise TypeError(f"Expected 'int', got {str(type(length))[7:-1]}")
    if length < 1:
        return {}

    # Build empty LinkedList of a specified number of elements
    first_node = create_node()
    curr = first_node

    for _ in range(length-1):
        curr['next'] = create_node()
        curr = curr['next']

    first_node['length'] = length
    first_node['last'] = curr
    return first_node


def print_linked_list(ll: 'a linked list object'):
    node = ll
    print(node['value'], end='')
    while node['next']:
        node = node['next']
        print(' ->', node['value'], end='')
    print()


def check_idx(idx: int, ll: 'a linked list object'):
    if not isinstance(idx, int):
        raise TypeError(f"Expected 'int', got {str(type(idx))[7:-1]}")
    if not 0 <= idx < ll['length']:
        raise IndexError(f"Index out of range")


def traverse_to_index(idx: int, ll: 'a linked list object'):
    check_idx(idx, ll)
    curr = ll
    for _ in range(idx):
        curr = curr['next']
    return curr


"""
***************
Other functions
***************
"""

def randomly_fill_linked_list(ll: 'a linked list object', min_num: int, max_num: int):
    curr = ll
    while True:
        curr['value'] = random.randint(min_num, max_num)
        if not curr['next']:
            break
        curr = curr['next']


def last_element_before_cycle(ll: 'a linked list object') -> dict:
    cycle_begin_item = ll['last']['next']

    curr = ll
    if curr is cycle_begin_item:
        return {}

    while curr['next'] is not cycle_begin_item:
        curr = curr['next']

    return curr


if __name__ == '__main__':
    ll = create_linked_list(15)
    randomly_fill_linked_list(ll, 0, 100)
    print_linked_list(ll)

    # We create a cycle by joining last element with one of the previous elements
    ll['last']['next'] = traverse_to_index(3, ll)
    print(ll['last']['next'])

    print(last_element_before_cycle(ll))
