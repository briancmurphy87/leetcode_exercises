from collections import defaultdict, Counter

from binary_tree.common_utils.get_index import get_child_index_left, get_child_index_right
from binary_tree.common_utils.init_array_from_bt import create_binary_tree_array_from_root_node
from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:        
"""

# class NodeSubTree:
#     def __init__(
#             self,
#             subtree_node_root: TreeNode,
#             subtree_node_values: list[list[TreeNode]],
#     ) -> None:
#         self.subtree_node_root = subtree_node_root
#         self.subtree_node_values = subtree_node_values
#
# def get_node_subtree(
#         node: TreeNodeWithIndex,
#         # output: list[list[TreeNodeWithIndex]],
#         node_subtree_indices: defaultdict[int, list[int]],
# ) -> list[TreeNodeWithIndex] | None:
#     if node.left is None and node.right is None:
#         return None
#
#     output: list[TreeNodeWithIndex] = []
#     # # TODO: DEBUG:
#     # node_subtree_indices: defaultdict[int, list[int]] = defaultdict(list)
#
#     if node.left is not None:
#         output.append(node.left)
#         lhs_node_subtree = get_node_subtree(node=node.left, node_subtree_indices=node_subtree_indices)
#         node_subtree_indices[node.node_array_index].append(node.left.node_array_index)
#         if lhs_node_subtree is not None:
#             node_subtree_indices[node.left.node_array_index].extend(lhs_node_subtree)[]
#         # if lhs_node_subtree is None:
#         #     x = 0
#         # if lhs_node_subtree is not None:
#         #     output.append(lhs_node_subtree)
#
#     if node.right is not None:
#         output[-1].append(node.right)
#         rhs_node_subtree = get_node_subtree(node=node.right, output=output)
#         if rhs_node_subtree is None:
#             node_subtree_indices[node.node_array_index].append(node.right.node_array_index)
#         # if rhs_node_subtree is not None:
#         #     output.append(rhs_node_subtree)
#
# def count_uni_val_subtrees(root: TreeNodeWithIndex | None) -> int:
#     if root is None:
#         return 0
#
#     node_subtree_indices: defaultdict[int, list[int]] = defaultdict(list)
#
#     output: list[list[TreeNodeWithIndex]] = [[]]
#     get_node_subtree(node=root, output=output, node_subtree_indices=node_subtree_indices)
#
#     # TODO: DEBUG:
#     return -1

def _check_identical_elements(tree_array: list[int | None]) -> tuple[int, int] | None:
    root_val: int | None = tree_array[0]
    assert root_val is not None

    is_identical_mask: list[bool] = [
        root_val == val
        for val in tree_array[1:] if val is not None
    ]
    if not all(is_identical_mask):
        return None

    # count number of instances that qualify
    # (add 1 to account for 'root node')
    uni_value_node_count = sum(is_identical_mask) + 1
    return root_val, uni_value_node_count


def count_uni_val_subtrees_from_array_impl(
    tree_array: list[int | None],
    root_node_index: int,
    subtree_node_index_lookups: defaultdict[int, list[int]],
) -> None:

    if root_node_index >= len(tree_array):
        return

    root_node_value: int | None = tree_array[root_node_index]
    assert root_node_value is not None

    lhs_node_index, rhs_node_index = [
        get_child_index(root_node_index)
        for get_child_index in (get_child_index_left, get_child_index_right)
    ]

    lhs_node_value, rhs_node_value = [
        None
        if child_node_index >= len(tree_array)
        else tree_array[child_node_index]
        for child_node_index in (lhs_node_index, rhs_node_index)
    ]

    for child_node_index, child_node_value in zip(
            (lhs_node_index, rhs_node_index),
            (lhs_node_value, rhs_node_value),
    ):
        if child_node_value is None:
            continue

        subtree_node_index_lookups[root_node_index].append(child_node_index)
        # TODO: search through it for subtrees
        count_uni_val_subtrees_from_array_impl(
            tree_array=tree_array,
            root_node_index=child_node_index,
            subtree_node_index_lookups=subtree_node_index_lookups,
        )


def count_uni_val_subtrees_from_array(
        tree_array: list[int | None],
) -> int:
    if not tree_array:
        return 0

    # trivial case -> all are the same value
    is_identical_check_opt: tuple[int, int] | None = (
        _check_identical_elements(tree_array)
    )
    if is_identical_check_opt is not None:
        _, uni_value_node_count = is_identical_check_opt
        return uni_value_node_count

    subtree_node_index_lookups: defaultdict[int, list[int]] = defaultdict(list)

    root_node_index = 0
    assert tree_array[root_node_index] is not None
    count_uni_val_subtrees_from_array_impl(
        tree_array=tree_array,
        root_node_index=root_node_index,
        subtree_node_index_lookups=subtree_node_index_lookups,
    )

    (
        uni_value_subtree_root_nodes,
        uni_value_subtree_root_nodes_deleted,
    ) = _update_collections_for_subtree_root_node_indices(
        tree_array=tree_array,
        subtree_node_index_lookups=subtree_node_index_lookups,
    )

    uni_value_counts = Counter()
    uni_value_counts.update(
        subtree_common_val
        for _, (subtree_common_val, subtree_common_val_count) in uni_value_subtree_root_nodes.items()
        for _ in range(subtree_common_val_count)
    )
    if not uni_value_counts:
        return 0
    else:
        return max(uni_value_counts.values())


def _update_collections_for_subtree_root_node_indices(
    tree_array: list[int | None],
    subtree_node_index_lookups: defaultdict[int, list[int]],
) -> tuple[
    dict[int, tuple[int, int]],
    dict[int, tuple[int, int]],
]:
    uni_value_subtree_root_nodes: dict[int, tuple[int, int]] = {}
    uni_value_subtree_root_nodes_deleted: dict[int, tuple[int, int]] = {}

    for subtree_root_node_index in sorted(subtree_node_index_lookups.keys(), reverse=True):
        _update_collections_for_subtree_root_node_index(
            subtree_root_node_index=subtree_root_node_index,
            tree_array=tree_array,
            subtree_node_index_lookups=subtree_node_index_lookups,
            uni_value_subtree_root_nodes=uni_value_subtree_root_nodes,
            uni_value_subtree_root_nodes_deleted=uni_value_subtree_root_nodes_deleted,
        )

    return uni_value_subtree_root_nodes, uni_value_subtree_root_nodes_deleted

def _update_collections_for_subtree_root_node_index(
    subtree_root_node_index: int,
    tree_array: list[int | None],
    subtree_node_index_lookups: defaultdict[int, list[int]],
    uni_value_subtree_root_nodes: dict[int, tuple[int, int]],
    uni_value_subtree_root_nodes_deleted: dict[int, tuple[int, int]],
) -> None:
    subtree_root_node_value: int | None = tree_array[subtree_root_node_index]
    assert subtree_root_node_value is not None

    subtree_is_leaves_only = True
    subtree_node_info_list: list[tuple[int, int, bool]] = []
    next_level_nodes_have_root_val = True
    for subtree_node_index in subtree_node_index_lookups[subtree_root_node_index]:
        if tree_array[subtree_node_index] is None:
            continue

        subtree_node_is_subtree_root = subtree_node_index in subtree_node_index_lookups
        subtree_node_info_list.append((
            subtree_node_index,
            tree_array[subtree_node_index],
            subtree_node_is_subtree_root,
        ))

        subtree_is_leaves_only = subtree_is_leaves_only and not subtree_node_is_subtree_root
        next_level_nodes_have_root_val = (
                next_level_nodes_have_root_val
                and tree_array[subtree_node_index] == subtree_root_node_value
        )

    if not subtree_is_leaves_only:
        for (subtree_node_index, subtree_node_value, subtree_node_is_subtree_root) in subtree_node_info_list:
            # get common value of the subtree rooted at this node (if any)
            if not (subtree_node_is_subtree_root and subtree_node_index in uni_value_subtree_root_nodes):
                continue

            (
                subtree_node_subtree_common_val,
                subtree_node_subtree_common_val_count,
            ) = uni_value_subtree_root_nodes[subtree_node_index]

            # is this node a continuation of its subtree's common value?
            if subtree_node_value != subtree_node_subtree_common_val:
                continue

            # insert new entry
            uni_value_count_new = subtree_node_subtree_common_val_count
            if next_level_nodes_have_root_val:
                uni_value_count_new += 1

            uni_value_subtree_root_nodes[subtree_root_node_index] = (
                subtree_node_subtree_common_val,
                uni_value_count_new,
            )
            # clear the old entry of the child node -> this node is now representative
            uni_value_subtree_root_nodes_deleted[subtree_node_index] = (
                uni_value_subtree_root_nodes[subtree_node_index]
            )
            del uni_value_subtree_root_nodes[subtree_node_index]

    else:
    # elif all(
    #         val == subtree_root_val
    #         for (_, val, _) in subtree_node_info_list[1:]
    # ):

        subtree_nodes_of_root_value: list[tuple[int, tuple[int, int, bool]]] = [
            (subtree_node_info_index, subtree_node_info)
            for subtree_node_info_index, subtree_node_info in enumerate(subtree_node_info_list)
            if subtree_node_info[1] is not None and subtree_node_info[1] == subtree_root_node_value
        ]

        subtree_value_counts: defaultdict[int, int] = defaultdict(int)

        subtree_value_count_max: int | None = None
        subtree_value_count_max_keys: set[int] = set()
        for (subtree_node_index, subtree_node_value, _) in (
                [
                    (
                            subtree_root_node_index,
                            subtree_root_node_value,
                            False,
                    )
                ] + subtree_node_info_list
        ):
            subtree_value_counts[subtree_node_value] += 1

            if subtree_value_count_max is None:
                subtree_value_count_max = subtree_value_counts[subtree_node_value]
                subtree_value_count_max_keys.add(subtree_node_value)

            elif subtree_value_count_max == subtree_value_counts[subtree_node_value]:
                subtree_value_count_max_keys.add(subtree_node_value)

            elif subtree_value_count_max < subtree_value_counts[subtree_node_value]:
                # new max
                subtree_value_count_max = subtree_value_counts[subtree_node_value]
                subtree_value_count_max_keys = {subtree_node_value}

        assert subtree_value_counts
        if subtree_value_count_max > 1:
            if subtree_root_node_value in subtree_value_count_max_keys:
                uni_value = subtree_root_node_value
            else:
                uni_value = next(iter(subtree_value_count_max_keys))
            uni_value_subtree_root_nodes[subtree_root_node_index] = (
                uni_value,
                subtree_value_count_max,
            )


def count_uni_vals(
        tree_array: list[int | None],
) -> int:
    if not tree_array:
        return 0

    sub_node_value_counts: defaultdict[int, int] = defaultdict(int)
    for sub_node_value in tree_array[1:]:
        sub_node_value_counts[sub_node_value] += 1

    max_count = max(sub_node_value_counts.values())
    max_count_keys = [
        val
        for val, val_count in sub_node_value_counts.items()
        if val_count == max_count
    ]
    root_value = tree_array[0]
    assert root_value is not None
    max_count_add = 0

    if root_value in max_count_keys:
        root_value_same_as_children = True
        for root_child_index in (1, 2):
            root_child_value = None if root_child_index >= len(tree_array) else tree_array[root_child_index]
            if root_child_value is not None and root_child_value != root_value:
                root_value_same_as_children = False
                break
        if root_value_same_as_children:
            max_count_add += 1

    return max_count + max_count_add

if __name__ == '__main__':

    # res = count_uni_vals([5,1,3,1,1,1])
    # res1 = count_uni_vals([5, 1, 5, 5, 5, None, 5])
    res2 = count_uni_vals([5,5,5,5,5,None,5])
    x = 0

    """
    Input: root = [5,1,5,5,5,null,5]
    Output: 4
    """
    # tree_array = [5,5,1]
    # result = count_uni_val_subtrees_from_array(tree_array)

    root_node1 = create_binary_tree_from_array([5, 1, 5, 5, 5, None, 5])
    tree_array1 = create_binary_tree_array_from_root_node(root_node1)
    assert tree_array1 == [5, 1, 5, 5, 5, None, 5]
    output1 = count_uni_val_subtrees_from_array(tree_array1)
    assert output1 == 4
    print(output1)

    # tree_array2 = [5,5,5,5,5,None,5]
    # output2 = count_uni_val_subtrees_from_array(tree_array2)

    # output1 = count_uni_val_subtrees(
    #     root=create_binary_tree_from_array([5, 1, 5, 5, 5, None, 5])
    # )
    # print(output2)