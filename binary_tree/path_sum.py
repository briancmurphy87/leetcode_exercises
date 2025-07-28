"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

"""
from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode


def has_path_sum_impl(
        root: TreeNode,
        rem_target_sum: int,
) -> bool:
    # # exceeded sum
    # if root.val > rem_target_sum:
    #     return False

    # is current node leaf? check if path sum works
    if root.left is None and root.right is None:
        res = root.val == rem_target_sum
        return res

    # otherwise, continue to traverse each subtree (where values exist)
    lhs_has_path_sum, rhs_has_path_sum = [
        False
        if child_node is None
        else has_path_sum_impl(
            root=child_node,
            rem_target_sum=rem_target_sum-root.val,
        )
        for child_node in (root.left, root.right)

    ]
    # evaluate if either subtree yielded a viable path
    return lhs_has_path_sum or rhs_has_path_sum

def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    if root is None:
        return False

    return has_path_sum_impl(
        root=root,
        rem_target_sum=target_sum,
    )

if __name__ == '__main__':
    """
    (EX1)
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.
    
    (EX2)
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There are two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.
    """
    root2 = [-2, None, -3]
    target_sum2 = -5
    output2 = has_path_sum(
        root=create_binary_tree_from_array(root2),
        target_sum=target_sum2,
    )

    root1 = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum1 = 22

    root_node1: TreeNode | None = create_binary_tree_from_array(root1)
    output1 = has_path_sum(root=root_node1, target_sum=targetSum1)
    print(output1)
