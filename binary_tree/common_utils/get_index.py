def get_parent_index(child_index: int) -> int:
    return child_index // 2


def get_child_index_left(root_index: int) -> int:
    return 2 * root_index + 1


def get_child_index_right(root_index: int) -> int:
    # lhs_index = get_child_index_left(root_index)
    # return lhs_index + 1
    return 2 * (root_index + 1)
