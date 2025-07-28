"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

"""
from typing import Literal

from binary_tree.common_utils.get_index import get_child_index_left
from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode

# class Solution:
#     def __init__(self) -> None:
#         p_path: list[int] = []
#         q_path: list[int] = []

RecurseOutcome = Literal[
    'nothing',
    'found_target',
    'found_lca',
]

def lowest_common_ancestor(
        root: TreeNode, p: TreeNode, q: TreeNode,
) -> TreeNode | None:
    node_index_root = 0
    result = lowest_common_ancestor_recurse(
        node_current=root,
        node_p=p,
        node_q=q,
        node_index_current=node_index_root,
    )
    if isinstance(result, TreeNode):
        return result
    else:
        return None

def lowest_common_ancestor_recurse(
        node_current: TreeNode | None,
        node_p: TreeNode,
        node_q: TreeNode,
        node_index_current: int,
) -> bool | TreeNode:
    # reached end of path
    if node_current is None:
        return False

    # check if current node is among target nodes
    found_target_at_current_node = node_current in [node_p, node_q]

    # search LEFT sub-tree
    left_index = get_child_index_left(node_index_current)
    found_target_in_left_tree = lowest_common_ancestor_recurse(
        node_current=node_current.left,
        node_p=node_p,
        node_q=node_q,
        node_index_current=left_index,
    )
    if isinstance(found_target_in_left_tree, TreeNode):
        return found_target_in_left_tree

    # search RIGHT sub-tree
    right_index = left_index + 1
    found_target_in_right_tree = lowest_common_ancestor_recurse(
        node_current=node_current.right,
        node_p=node_p,
        node_q=node_q,
        node_index_current=right_index,
    )
    if isinstance(found_target_in_right_tree, TreeNode):
        return found_target_in_right_tree

    # count 'bool' flags to see if we have found ALL target nodes
    found_sum = sum([found_target_at_current_node, found_target_in_left_tree, found_target_in_right_tree])
    if found_sum >= 2:
        return node_current

    # return 'True' if any of the 'find flags' evaluated to 'True'
    return found_sum > 0

if __name__ == '__main__':

    tree_array, p_val, q_val = (
        [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
        5,
        1,
    )

    p_index, q_index = (
        tree_array.index(p_val),
        tree_array.index(q_val),
    )
    target_node_lookup: dict[int, TreeNode | None]
    tree_root, target_node_lookup = create_binary_tree_from_array(
        tree_array=tree_array,
        other_nodes_returned_indices=frozenset(
            [p_index, q_index],
        ),
    )

    p_node = target_node_lookup[p_index]
    q_node = target_node_lookup[q_index]

    lca_node = lowest_common_ancestor(root=tree_root, p=p_node, q=q_node)
    assert lca_node is not None
    print(lca_node.val)