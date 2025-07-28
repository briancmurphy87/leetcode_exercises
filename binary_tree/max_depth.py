# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         pass
from binary_tree.common_utils.tree_node import TreeNode


def max_depth_top_down_impl(
        root: TreeNode | None,
        depth_output: int,
        depth_current: int,
) -> None:
    if root is None:
        return

    if root.left is None and root.right is None:
        depth_output = max(depth_output, depth_current)

    max_depth_top_down_impl(root=root.left, depth_output=depth_output, depth_current=depth_current + 1)
    max_depth_top_down_impl(root=root.right, depth_output=depth_output, depth_current=depth_current + 1)

def max_depth_top_down(
        root: TreeNode | None,
) -> int:
    depth_output: int = 0
    max_depth_top_down_impl(root=root, depth_output=depth_output, depth_current=0)
    return depth_output


def max_depth_bottom_up(
        root: TreeNode | None,
) -> int:
    if root is None:
        return 0

    depth_left = max_depth_bottom_up(root.left)
    depth_right = max_depth_bottom_up(root.right)

    # return depth of the subtree rooted at root
    return max(depth_left, depth_right) + 1

if __name__ == '__main__':
    pass
# Input: root = [3,9,20,null,null,15,7]
# Output: 3