"""
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees
"""
import operator
from typing import Optional, NamedTuple

from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_bst(root)

SubTreeMinMax = tuple[int | None, int | None]
LeftAndRightSubTreeMinMax = tuple[SubTreeMinMax, SubTreeMinMax]


def is_valid_bst(
    root: TreeNode | None,
) -> bool:
    if root is None:
        return False
    # is_valid, (new_sub_tree_min, new_sub_tree_max) = (
    #     is_valid_bst_helper(root=root, sub_tree_min=None, sub_tree_max=None)
    # )
    is_valid, _ = (
        is_valid_bst_helper(root=root, sub_tree_min=None, sub_tree_max=None)
    )
    return is_valid

    # lhs_sub_tree_max: int | None = None
    # rhs_sub_tree_min: int | None = None
    #
    # # explict invalidation
    # if root.left is not None and root.left.val >= root.val:
    #     return False
    #
    # if root.right is not None and root.right.val <= root.val:
    #     return False
    #
    # lhs_check_output = is_valid_bst_helper(root=root.left, get_max=True)
    # if isinstance(lhs_check_output, bool) and not lhs_check_output:
    #     return False
    # if isinstance(lhs_check_output, int):
    #     lhs_sub_tree_max = lhs_check_output
    #
    # rhs_check_output = is_valid_bst_helper(root=root.right, get_max=False)
    # if isinstance(rhs_check_output, bool) and not rhs_check_output:
    #     return False
    # if isinstance(rhs_check_output, int):
    #     rhs_sub_tree_min = rhs_check_output
    #
    # if lhs_sub_tree_max and lhs_sub_tree_max >= root.val:
    #     return False
    #
    # if rhs_sub_tree_min and rhs_sub_tree_min <= root.val:
    #     return False
    #
    # return True

def _safe_min_or_max(values: list[int | None], is_min: bool) -> int | None:
    if is_min:
        return min((x for x in values if x is not None), default=None)
    else:
        return max((x for x in values if x is not None), default=None)


def safe_min(values: list[int | None]) -> int | None:
    return _safe_min_or_max(values=values, is_min=True)


def safe_max(values: list[int | None]) -> int | None:
    return _safe_min_or_max(values=values, is_min=False)


def is_valid_bst_helper(
    root: TreeNode | None,
    sub_tree_min: int | None,
    sub_tree_max: int | None,
) -> tuple[bool, SubTreeMinMax]:

    if root is None:
        return True, (None, None)

    # # update subtree min/max
    # sub_tree_min = safe_min(values=[
    #     sub_tree_min,
    #     root.val,
    #     # (root.left and root.left.val),
    #     # (root.right and root.right.val),
    # ])
    # sub_tree_max = safe_max(values=[
    #     sub_tree_max,
    #     root.val,
    #     # (root.left and root.left.val),
    #     # (root.right and root.right.val),
    # ])

    # explict invalidation?
    for child_node, node_val_binary in zip((root.left, root.right), (operator.ge, operator.le)):
        if child_node is not None and node_val_binary(child_node.val, root.val):
            # return invalidation state
            return (
                False,
                (
                    sub_tree_min,
                    sub_tree_max,
                )
            )

    # if root.left is not None and root.left.val >= root.val:
    #     sub_tree_min = safe_min(values=[sub_tree_min, root.val, root.left.val])
    #     sub_tree_max = safe_max(values=[sub_tree_max, root.val, root.right.val])
    #     return False, sub_tree_min, sub_tree_max

    # if root.right is not None and root.right.val <= root.val:
    #     if sub_tree_min is None:
    #         sub_tree_min = root.right.val
    #     else:
    #         sub_tree_min = min(sub_tree_min, root.right.val)
    #
    #     if sub_tree_max is None:
    #         sub_tree_max = root.right.val
    #     else:
    #         sub_tree_max = max(sub_tree_max, root.right.val)
    #
    #     return False, sub_tree_min, sub_tree_max

    lhs_is_valid, lhs_sub_tree_min_max = is_valid_bst_helper(
        root=root.left,
        sub_tree_min=sub_tree_min,
        sub_tree_max=sub_tree_max,
        # sub_tree_min=safe_min(values=[sub_tree_min, (root.left and root.left.val)]),
        # sub_tree_max=safe_max(values=[sub_tree_max, (root.left and root.left.val)]),
    )
    rhs_is_valid, rhs_sub_tree_min_max = is_valid_bst_helper(
        root=root.right,
        sub_tree_min=sub_tree_min,
        sub_tree_max=sub_tree_max,
        # sub_tree_min=safe_min(values=[sub_tree_min, (root.right and root.right.val)]),
        # sub_tree_max=safe_max(values=[sub_tree_max, (root.right and root.right.val)]),
    )

    sub_tree_invalid = (
            not (lhs_is_valid and rhs_is_valid)
            or (lhs_sub_tree_min_max[1] is not None and lhs_sub_tree_min_max[1] >= root.val)
            or (rhs_sub_tree_min_max[0] is not None and rhs_sub_tree_min_max[0] <= root.val)
    )

    all_values = list((root.val,) + lhs_sub_tree_min_max + rhs_sub_tree_min_max)
    new_sub_tree_max = safe_max(values=all_values)
    new_sub_tree_min = safe_min(values=all_values)

    return (
        (not sub_tree_invalid),
        (
            new_sub_tree_min,
            new_sub_tree_max,
        ),
    )

    # if not (lhs_is_valid and rhs_is_valid):
    #     return False, new_lhs_sub_tree_max, new_rhs_sub_tree_min
    # elif lhs_sub_tree_max >= root.val:
    #     return False, new_lhs_sub_tree_max, new_rhs_sub_tree_min
    # elif rhs_sub_tree_min <= root.val:
    #     return False, new_lhs_sub_tree_max, new_rhs_sub_tree_min
    # if lhs_is_valid and rhs_is_valid:
    #     return True, lhs_sub_tree_max, rhs_sub_tree_min
    # else:
    #     return False, lhs_sub_tree_max, rhs_sub_tree_min
    # if not (lhs_is_valid and rhs_is_valid):
    #     return False, lhs_sub_tree_max, rhs_sub_tree_min
    #
    # if lhs_sub_tree_max >= root.val:
    #     return False, lhs_sub_tree_max, rhs_sub_tree_min
    #
    # if rhs_sub_tree_min <= root.val:
    #     return False, lhs_sub_tree_max, rhs_sub_tree_min



# def is_valid_bst_helper(
#     root: TreeNode | None,
#     get_max: bool,
# ) -> bool | int | None:
#     if root is None:
#         return True
#
#     lhs_value: int | None = None
#     rhs_value: int | None = None
#
#     if root.left is not None:
#         # explict invalidation
#         if root.left.val >= root.val:
#             return False
#
#         # else:
#         lhs_check_output = is_valid_bst_helper(root=root.left, get_max=get_max)
#         if lhs_check_output is False:
#             return False
#
#
#     if root.right is not None:
#         if root.right.val <= root.val:
#             return False
#         # else:
#         # rhs_valid = is_valid_bst(root.right)
#         rhs_check_output = is_valid_bst_helper(root=root.right, get_max=get_max)
#         if rhs_check_output is False:
#             return False
#
#
#     return lhs_valid and rhs_valid

if __name__ == "__main__":
    """
    Input: root = [2,1,3]
    Output: true
    """
    # root_node, _  = create_binary_tree_from_array(tree_array=[2, 1, 3])
    # root_node, _ = create_binary_tree_from_array(tree_array=[5,1,4,None,None,3,6])
    root_node, _ = create_binary_tree_from_array(tree_array=[5,4,6,2,8,3,7])
    print(is_valid_bst(root=root_node))