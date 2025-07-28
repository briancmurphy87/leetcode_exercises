# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Codec:
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#
#         :type data: str
#         :rtype: TreeNode
#         """
#
#
# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))
import json
from collections import defaultdict
from typing import Any, NamedTuple

# from pydantic import BaseModel

from binary_tree.common_utils.get_index import get_child_index_left, get_child_index_right
from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node import TreeNode
from binary_tree.traversal.level_order_v3 import traverse_level_order_v3


class TreeNodeBaseModel(NamedTuple):
    val: int
    index: int
    left_index: int | None
    right_index: int | None


def init_tree_node_model(node: TreeNode, node_index: int) -> TreeNodeBaseModel:
    node_index_left = None if node.left is None else get_child_index_left(node_index)
    node_index_right = None if node.right is None else get_child_index_right(node_index)
    return TreeNodeBaseModel(
        val=node.val,
        index=node_index,
        left_index=node_index_left,
        right_index=node_index_right,
    )


def serialize_binary_tree(root_node: TreeNode | None) -> str:
    if root_node is None:
        return "[]"

    traversal_output = traverse_level_order_v3(root_node)


    output_v2: defaultdict[int, list[dict[str, Any]]] = defaultdict(list)

    max_level_index = max(traversal_output.level_index_to_level_node_indices.keys())
    for level_index in range(0, max_level_index + 1):
        # output.append([])
        for node_index in traversal_output.level_index_to_level_node_indices[level_index]:
            node: TreeNode | None = traversal_output.tree_array_index_to_node[node_index]
            if node is not None:
                # output[level_index].append({})
            # else:
                tree_node_model = init_tree_node_model(node=node, node_index=node_index)
                tree_node_model_data = tree_node_model._asdict()
                # output[level_index].append(tree_node_model_data)
                output_v2[level_index].append(tree_node_model_data)
    output: list[list[dict[str, Any]]] = [
        output_v2[level_index]
        for level_index in range(0, max_level_index + 1)
    ]

    return json.dumps(output)


def deserialize_binary_tree(data: str) -> TreeNode | None:
    data_json = json.loads(data)
    assert isinstance(data_json, list)

    level_count = len(data_json)
    if level_count == 0:
        return None

    node_array_index_to_node: dict[int, TreeNode] = {}

    last_level_index = level_count - 1
    last_level_values_json: list[dict[str, Any]] = data_json[last_level_index]
    for tree_node_data in last_level_values_json[::-1]:
        if not tree_node_data:
            continue
        tree_node_model = TreeNodeBaseModel(**tree_node_data)
        assert tree_node_model.left_index is None
        assert tree_node_model.right_index is None

        node_array_index_to_node[tree_node_model.index] = TreeNode(
            val=tree_node_model.val,
            left=None,
            right=None,
        )

    for level_index_rev in range(last_level_index - 1, -1, -1):
        level_values_json: list[dict[str, Any]] = data_json[level_index_rev]
        for tree_node_data in level_values_json[::-1]:
            tree_node_model = TreeNodeBaseModel(**tree_node_data)
            assert tree_node_model.index not in node_array_index_to_node

            tree_node_left, tree_node_right = [
                None
                if child_index is None
                else node_array_index_to_node[child_index]
                for child_index in (tree_node_model.left_index, tree_node_model.right_index)
            ]
            node_array_index_to_node[tree_node_model.index] = TreeNode(
                val=tree_node_model.val,
                left=tree_node_left,
                right=tree_node_right,
            )

    # return root node
    return node_array_index_to_node[0]

if __name__ == '__main__':
    output_serialized = serialize_binary_tree(None)
    output_deserialized = deserialize_binary_tree(output_serialized)

    root = [1, 2, 3, None, None, 4, 5]
    root_node, _ = create_binary_tree_from_array(root)
    output_serialized = serialize_binary_tree(root_node)
    output_deserialized = deserialize_binary_tree(output_serialized)
