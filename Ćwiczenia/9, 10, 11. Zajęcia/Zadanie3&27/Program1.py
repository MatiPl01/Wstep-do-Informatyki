# Functions-based implementation

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


"""
***************
Other functions
***************
"""


def get_sorted_random_int_list(length: int, min_num: int, max_num: int) -> [int]:
    return sorted(random.randint(min_num, max_num) for _ in range(length))


def fill_linked_list(ll: 'a linked list object', seq: 'a sequence of elements'):
    if len(seq) != ll['length']:
        raise ValueError(f"Passed sequence's length ({len(seq)}) doesn't match a length of a linked list ({ll['length']})")

    curr = ll
    for val in seq:
        curr['value'] = val
        curr = curr['next']


def get_merged_linked_lists_iter(ll1: 'a sorted linked list', ll2: 'a sorted linked list') -> 'a merged linked list':
    ll_merged = create_linked_list(ll1['length'] + ll2['length'])

    ll_merged_curr = ll_merged
    ll1_curr = ll1
    ll2_curr = ll2

    while ll1_curr or ll2_curr:
        if ll1_curr and ll2_curr:
            if ll1_curr['value'] <= ll2_curr['value']:
                ll_merged_curr['value'] = ll1_curr['value']
                ll1_curr = ll1_curr['next']
            else:
                ll_merged_curr['value'] = ll2_curr['value']
                ll2_curr = ll2_curr['next']

        elif ll1_curr:
            ll_merged_curr['value'] = ll1_curr['value']
            ll1_curr = ll1_curr['next']
        else:
            ll_merged_curr['value'] = ll2_curr['value']
            ll2_curr = ll2_curr['next']

        ll_merged_curr = ll_merged_curr['next']

    return ll_merged


def get_merged_linked_lists_recur(ll1: 'a sorted linked list', ll2: 'a sorted linked list') -> 'a merged linked list':
    ll_merged = create_linked_list(ll1['length'] + ll2['length'])

    def recur(ll_merged_curr=ll_merged, ll1_curr=ll1, ll2_curr=ll2):
        if not (ll1_curr or ll2_curr):
            return

        if ll1_curr and ll2_curr:
            if ll1_curr['value'] <= ll2_curr['value']:
                ll_merged_curr['value'] = ll1_curr['value']
                ll1_curr = ll1_curr['next']
            else:
                ll_merged_curr['value'] = ll2_curr['value']
                ll2_curr = ll2_curr['next']

        elif ll1_curr:
            ll_merged_curr['value'] = ll1_curr['value']
            ll1_curr = ll1_curr['next']
        else:
            ll_merged_curr['value'] = ll2_curr['value']
            ll2_curr = ll2_curr['next']

        ll_merged_curr = ll_merged_curr['next']

        recur(ll_merged_curr, ll1_curr, ll2_curr)

    recur()

    return ll_merged


if __name__ == '__main__':
    ll1_items = get_sorted_random_int_list(10, 0, 100)
    ll2_items = get_sorted_random_int_list(6, 5, 20)

    # Create the first linked list
    ll1 = create_linked_list(len(ll1_items))
    fill_linked_list(ll1, ll1_items)
    print_linked_list(ll1)

    # Create the second linked list
    ll2 = create_linked_list(len(ll2_items))
    fill_linked_list(ll2, ll2_items)
    print_linked_list(ll2)

    # An iterative solution
    ll_merged_iter = get_merged_linked_lists_iter(ll1, ll2)
    print_linked_list(ll_merged_iter)

    # A recursive solution
    ll_merged_recur = get_merged_linked_lists_recur(ll1, ll2)
    print_linked_list(ll_merged_iter)
