"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
"""

from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode
from binary_tree.traversal.level_order import traverse_level_order, traverse_level_order_v2


def is_symmetric(root_node: TreeNode | None) -> bool:
    # lhs_tree_root_node = root_node.left
    # rhs_tree_root_node = root_node.right
    # if lhs_tree_root_node is None and rhs_tree_root_node is None:
    #     return True

    tree_levels: list[list[int]] = traverse_level_order(root_node)
    if not tree_levels:
        return False

    for tree_level_index, tree_level_values in enumerate(tree_levels):
        pass

    return False


def is_symmetric_at_level(
        # level_index: int,
        level_index_values: list[int | None],
) -> bool:
    level_values_len = len(level_index_values)
    # assert level_values_len % 2 == 0
    index_mid = level_values_len // 2

    lhs_values = level_index_values[:index_mid]
    rhs_values = level_index_values[index_mid:]
    # assert len(lhs_values) == len(rhs_values)

    return lhs_values == rhs_values[::-1]

def is_symmetric_impl(levels: list[list[int | None]]) -> bool:
    level_root = levels[0]
    assert len(level_root) == 1

    for level_index, level_values in enumerate(levels[1:]):
        if not is_symmetric_at_level(level_values):
            return False
    return True

if __name__ == '__main__':
    root = [1, 2, 2, 2, None, 2]
    test = is_symmetric_impl(
        levels=traverse_level_order_v2(
            root=create_binary_tree_from_array(root)
        )
    )
    """
    ex1
    Input: root = [1,2,2,3,4,4,3]
    Output: true

    ex2
    Input: root = [1,2,2,null,3,null,3]
    Output: false
    """
    # ex2
    root2 = [1,2,2, None, 3, None, 3]
    root_node2: TreeNode | None = create_binary_tree_from_array(root2)

    traverse_level2 = traverse_level_order_v2(root_node2)
    # output2 = is_symmetric(root_node2)
    output2 = is_symmetric_impl(traverse_level2)
    print(output2)

    # ex1
    root1 = [1,2,2,3,4,4,3]
    root_node1: TreeNode | None = create_binary_tree_from_array(root1)
    traverse_level1 = traverse_level_order_v2(root_node1)
    output1 = is_symmetric_impl(traverse_level1)
    print(output1)