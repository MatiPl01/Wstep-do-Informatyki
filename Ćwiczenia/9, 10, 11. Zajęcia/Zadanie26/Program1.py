# Functions-based implementation
# I assume that when a linked list is a subsequence of another linked list, its elements are included
# in this linked list in order without any breaks between them
# e.g. 1 -> 2 -> 3 -> 4 -> 5 includes 2 -> 3 -> 4 but not 2 -> 3 -> 5 because we would have to skip 4

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

def fill_linked_list(ll: 'a linked list object', seq: 'a sequence of elements'):
    if len(seq) != ll['length']:
        raise ValueError(f"Passed sequence's length ({len(seq)}) doesn't match a length of a linked list ({ll['length']})")

    curr = ll
    for val in seq:
        curr['value'] = val
        curr = curr['next']


def found_list(ll1_curr, ll2_curr) -> bool:
    # ll2 linked list will never be longer than the ll1 so either both lists are exhausted
    # or the ll2 is exhausted. In both cases we had to iterate over all of the values in the ll2
    # so we are sure that a matching list was found
    while ll2_curr['next']:
        if ll1_curr['next']['value'] != ll2_curr['next']['value']:
            return False
        ll1_curr = ll1_curr['next']
        ll2_curr = ll2_curr['next']

    return True


def includes_linked_list(ll1: 'a longer linked list object', ll2: 'a shorter linked list object') -> bool:
    if ll1['length'] < ll2['length']:
        raise ValueError(f"The first linked list passed cannot include the second one as it is longer that the first one")

    ll1_curr = ll1
    for _ in range(ll1['length'] - ll2['length'] + 1):  # Iterate till we are able to find a matching subsequence
        if ll1_curr['value'] == ll2['value'] and found_list(ll1_curr, ll2):
            return True

        ll1_curr = ll1_curr['next']

    return False


if __name__ == '__main__':
    ll1_items = 1, 2, 6, 3, 4, 5, 9, 2, 3, 4
    ll2_items = 2, 3, 4

    # Create the first linked list
    ll1 = create_linked_list(len(ll1_items))
    fill_linked_list(ll1, ll1_items)
    print_linked_list(ll1)

    # Create the second linked list
    ll2 = create_linked_list(len(ll2_items))
    fill_linked_list(ll2, ll2_items)
    print_linked_list(ll2)

    print(includes_linked_list(ll1, ll2))
