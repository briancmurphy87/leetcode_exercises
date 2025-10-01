from typing import Optional

from binary_tree.common_utils.tree_node import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return search_bst_helper(root, val)

def search_bst_helper(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None

    if root.val == val:
        return root

    elif root.val > val:
        # go left
        return root.left and search_bst_helper(root=root.left, val=val)

    else: # root.val < p.val
        # go right
        return root.right and search_bst_helper(root=root.right, val=val)