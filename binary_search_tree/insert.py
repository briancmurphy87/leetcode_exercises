from typing import Optional

from binary_tree.common_utils.init_array_from_bt import create_binary_tree_array_from_root_node
from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode
from binary_tree.serialization import TreeNodeBaseModel


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return insert_bst(root, val)

def insert_bst(root: Optional[TreeNode], new_node_val: int) -> Optional[TreeNode]:
    if root is None:
        return TreeNode(new_node_val)

    insert_bst_helper(root, new_node_val)
    return root

def insert_bst_helper(root: TreeNode, new_node_val: int) -> None:

    assert root.val != new_node_val

    if root.val > new_node_val:
        # go left
        if root.left is None:
            root.left = TreeNode(new_node_val)
        else:
            insert_bst_helper(root.left, new_node_val)

    else: # root.val < p.val
        # go right
        if root.right is None:
            root.right = TreeNode(new_node_val)
        else:
            insert_bst_helper(root.right, new_node_val)


if __name__ == '__main__':
    """
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]
    """
    root_node, _ = create_binary_tree_from_array([4,2,7,1,3])
    output_node = insert_bst(root=root_node, new_node_val=5)
    print(create_binary_tree_array_from_root_node(output_node))