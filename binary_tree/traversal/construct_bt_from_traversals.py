"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

"""
from unittest.util import unorderable_list_difference

from binary_tree.common_utils.init_array_from_bt import create_binary_tree_array_from_root_node
from binary_tree.common_utils.tree_node import TreeNode
from binary_tree.traversal import post_order


def build_tree_helper(
        in_order: list[int],
        post_order: list[int],
        debug_mode: bool,
) -> TreeNode | None:
    if not post_order:
        return None

    assert len(in_order) == len(post_order)
    val_count = len(in_order)

    root_value = post_order[-1]
    root_value_in_order_index = in_order.index(root_value)

    in_order_left_tree_indices: tuple[int, int] = (
        0,
        root_value_in_order_index,
    )
    in_order_right_tree_indices: tuple[int, int] = (
        root_value_in_order_index + 1,
        val_count,
    )

    in_order_left, in_order_right = [
        in_order[subtree_index_start:subtree_index_finish]
        for (subtree_index_start, subtree_index_finish) in (
            in_order_left_tree_indices,
            in_order_right_tree_indices,
        )
    ]

    post_order_left_tree_indices = 0, len(in_order_left)
    post_order_right_tree_indices = len(in_order_left), -1
    post_order_left, post_order_right = [
        post_order[subtree_index_start:subtree_index_finish]
        for (subtree_index_start, subtree_index_finish) in (
            post_order_left_tree_indices,
            post_order_right_tree_indices,
        )
    ]

    if debug_mode:
        assert frozenset(in_order_left) == frozenset(post_order_left)
        assert frozenset(in_order_right) == frozenset(post_order_right)

    return TreeNode(
        val=root_value,
        left=build_tree_helper(
            in_order=in_order_left,
            post_order=post_order_left,
            debug_mode=debug_mode,
        ),
        right=build_tree_helper(
            in_order=in_order_right,
            post_order=post_order_right,
            debug_mode=debug_mode,
        ),
    )


def build_tree(
        in_order: list[int],
        post_order: list[int],
        debug_mode: bool = True,
) -> TreeNode | None:
    return build_tree_helper(
        in_order=in_order,
        post_order=post_order,
        debug_mode=debug_mode,
    )


def build_tree_pre_and_in_helper(
        pre_order: list[int],
        in_order: list[int],
        debug_mode: bool,
) -> TreeNode | None:
    if not pre_order:
        return None

    root_value = pre_order[0]
    root_value_in_order_index = in_order.index(root_value)

    in_order_left = in_order[:root_value_in_order_index]
    in_order_right = in_order[(root_value_in_order_index + 1):]

    pre_order_left = pre_order[1:(1 + len(in_order_left))]
    pre_order_right = pre_order[(1 + len(in_order_left)):]

    if debug_mode:
        assert frozenset(in_order_left) == frozenset(pre_order_left)
        assert frozenset(in_order_right) == frozenset(pre_order_right)

    return TreeNode(
        val=root_value,
        left=build_tree_pre_and_in_helper(
            pre_order=pre_order_left,
            in_order=in_order_left,
            debug_mode=debug_mode,
        ),
        right=build_tree_pre_and_in_helper(
            pre_order=pre_order_right,
            in_order=in_order_right,
            debug_mode=debug_mode,
        ),
    )

def build_tree_pre_and_in(
        pre_order: list[int],
        in_order: list[int],
        debug_mode: bool = True,
) -> TreeNode | None:
    return build_tree_pre_and_in_helper(
        pre_order=pre_order,
        in_order=in_order,
        debug_mode=debug_mode,
    )
if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    output_root_node = build_tree_pre_and_in(preorder, inorder)
    output_tree_array = create_binary_tree_array_from_root_node(output_root_node)
    print(output_tree_array)

    """
    Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
    Output: [3,9,20,null,null,15,7]
    """
    output_root_node1 = build_tree(in_order=[9,3,15,20,7], post_order=[9,15,7,20,3])
    output_tree_array1 = create_binary_tree_array_from_root_node(output_root_node1)
    print(output_tree_array1)