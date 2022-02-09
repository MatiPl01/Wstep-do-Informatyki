# Functions-based implementation

create_node = lambda value=0: {'value': value, 'next': None}


def init_linked_list(length: int) -> dict:
    if not isinstance(length, int):
        raise TypeError(f"Expected 'int', got {str(type(length))[7:-1]}")

    # Build empty LinkedList of a specified number of elements
    first_node = create_node()
    curr = first_node

    for _ in range(length-1):
        curr['next'] = create_node()
        curr = curr['next']

    first_node['length'] = length
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
    if idx >= ll['length']:
        raise IndexError(f"Index out of range")


def traverse_to_index(idx: int, ll: 'a linked list object'):
    check_idx(idx, ll)
    curr = ll
    for _ in range(idx):
        curr = curr['next']
    return curr


def get_value(idx: int, ll: 'a linked list object'):
    return traverse_to_index(idx, ll)['value']


def set_value(value, idx: int, ll: 'a linked list object'):
    traverse_to_index(idx, ll)['value'] = value


if __name__ == '__main__':
    ll = init_linked_list(5)
    print(ll)
    print_linked_list(ll)
    set_value(12, 2, ll)
    set_value(True, 1, ll)
    print(get_value(1, ll))
    # set_value('Something', 123, ll)
    print_linked_list(ll)
