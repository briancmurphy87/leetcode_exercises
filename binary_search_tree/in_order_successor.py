"""
apply the property of the BST
we have learned
to find out a better way to solve this problem.
"""
from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x: int) -> None:
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        return in_order_successor_helper(root, p)

def in_order_successor_helper(
        root: TreeNode,
        p: TreeNode,
) -> TreeNode | None:
    if root.val == p.val:
        return root.right and in_order_successor_helper(root=root.right, p=p)

    elif root.val > p.val:
        lhs_in_order_successor = root.left and in_order_successor_helper(root=root.left, p=p)
        if lhs_in_order_successor is not None and lhs_in_order_successor.val < root.val:
            return lhs_in_order_successor
        else:
            return root

    else: # root.val < p.val
        return root.right and in_order_successor_helper(root=root.right, p=p)

if __name__ == "__main__":
    root_node, _ = create_binary_tree_from_array([2,1,3])
    output_node = in_order_successor_helper(root=root_node, p=TreeNode(1))
    print(output_node.val)