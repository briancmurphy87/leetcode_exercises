# Definition for a binary tree node.
from collections import defaultdict
from typing import NamedTuple

from binary_tree.common_utils.get_index import get_child_index_left, get_child_index_right
from binary_tree.common_utils.tree_node import TreeNode
from binary_tree.common_utils.tree_node_next import Node


# TODO: this is breadth-first-search (BFS)
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

# BfsTreeNodeColor = Literal["white", "gray", "black"]
# class BfsTreeNode:
#     def __init__(
#             self,
#             val: int=0,
#             color: BfsTreeNodeColor = "white",
#             parent: Optional["BfsTreeNode"] = None,
#             distance: int = -1,
#     ):
#         self.val = val
#         self.color = color
#         self.parent = parent
#         self.distance = distance
#
# def breadth_first_search(root: BfsTreeNode | None) -> list[int]:
#
#
#     # mark attributes of root node
#     root.color = "gray"
#     root.distance = 0
#
#     # init queue with root
#     queue = deque[BfsTreeNode]()
#     queue.append(root)
#
#     # recurse while queue is not empty
#     while queue:
#         node_u = queue.popleft()

def traverse_level_order_helper(node: TreeNode | None, levels: list[list[int]], level_index: int) -> None:
    levels_len = len(levels)
    if levels_len == level_index:
        levels.append([])

    levels[level_index].append(node.val)

    if node.left is not None:
        traverse_level_order_helper(node.left, levels, level_index + 1)

    if node.right is not None:
        traverse_level_order_helper(node.right, levels, level_index + 1)


def traverse_level_order_impl(root: TreeNode | None, levels: list[list[int]]) -> list[list[int]]:

    if root is None:
        return levels

    traverse_level_order_helper(root, levels, 0)

    return levels

def traverse_level_order(root: TreeNode | None) -> list[list[int]]:
    levels: list[list[int]] = []
    return traverse_level_order_impl(root, levels)


def traverse_level_order_v2_helper(
        node: TreeNode | None,
        level_index: int,
        levels_lookup: defaultdict[int, list[int | None]],
) -> None:
    node_value_left, node_value_right = [
        None if node_child is None else node_child.val
        for node_child in (node.left, node.right)
    ]
    levels_lookup[level_index].append(node_value_left)
    levels_lookup[level_index].append(node_value_right)

    next_level_index = level_index + 1
    if node.left is not None:
        traverse_level_order_v2_helper(node.left, next_level_index, levels_lookup)

    if node.right is not None:
        traverse_level_order_v2_helper(node.right, next_level_index, levels_lookup)


def traverse_level_order_v2_impl(
        root: TreeNode | None,
) -> defaultdict[int, list[int | None]]:
    levels_lookup: defaultdict[int, list[int | None]] = defaultdict(list)

    root_value = None if root is None else root.val
    levels_lookup[0].append(root_value)

    traverse_level_order_v2_helper(node=root, level_index=1, levels_lookup=levels_lookup)
    return levels_lookup

def traverse_level_order_v2(root: TreeNode | None) -> list[list[int | None]]:
    levels_lookup: defaultdict[int, list[int | None]] = traverse_level_order_v2_impl(root)

    return [
        levels_lookup[level_index]
        for level_index in range(0, len(levels_lookup.keys()))
    ]


