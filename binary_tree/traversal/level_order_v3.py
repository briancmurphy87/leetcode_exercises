from collections import defaultdict
from typing import NamedTuple

from binary_tree.common_utils.get_index import get_child_index_left
from binary_tree.common_utils.tree_node_next import Node


class TraverseLevelOrderOutput(NamedTuple):
    level_index_to_level_node_indices: defaultdict[int, list[int | None]]
    tree_array_index_to_node: defaultdict[int, Node | None]

def build_list_of_values_from_traversal_output(
        traversal_output: TraverseLevelOrderOutput,
) -> list[list[int | None]]:

    max_level = max(traversal_output.level_index_to_level_node_indices.keys())
    output_levels: list[list[int | None]] = (
        (
            lambda get_val:  # outer lambda
            [
                [
                    get_val(node_index)
                    for node_index in traversal_output.level_index_to_level_node_indices[level_index]
                ]
                for level_index in range(0, max_level + 1)
            ]
        )
        (
            lambda node_index:  # inner lambda
            (
                node := traversal_output.tree_array_index_to_node.get(node_index)
            ) and node.val
        )
    )
    return output_levels


def traverse_level_order_v3(
        root_node: Node | None,
) -> TraverseLevelOrderOutput:

    output_levels_lookup, output_node_by_index = traverse_level_order_v3_impl(root_node=root_node)
    return TraverseLevelOrderOutput(
        level_index_to_level_node_indices=output_levels_lookup,
        tree_array_index_to_node=output_node_by_index,
    )

def traverse_level_order_v3_impl(
        root_node: Node | None,
) -> tuple[defaultdict[int, list[int | None]], defaultdict[int, Node | None]]:
    # output_tree_array: list[int | None] = []
    output_levels_lookup: defaultdict[int, list[int]] = defaultdict(list)
    output_node_by_index: defaultdict[int, Node | None] = defaultdict(lambda: None)

    # root_value = None if root_node is None else root_node.val
    # output_tree_array.append(root_value)
    output_levels_lookup[0].append(0)
    output_node_by_index[0] = root_node

    traverse_level_order_v3_helper(
        node=root_node,
        level_index=1,
        parent_node_array_index=0,
        # output_tree_array=output_tree_array,
        output_levels_lookup=output_levels_lookup,
        output_node_by_index=output_node_by_index,
    )
    return output_levels_lookup, output_node_by_index

def traverse_level_order_v3_helper(
        node: Node | None,
        level_index: int,
        parent_node_array_index: int,
        output_levels_lookup: defaultdict[int, list[int | None]],
        output_node_by_index: dict[int, Node | None],
) -> None:
    # is leaf?
    if node is None:
        return
    if node.left is None and node.right is None:
        return

    # node not a leaf -> unpack child nodes
    left_node_index = get_child_index_left(parent_node_array_index)
    right_node_index = left_node_index + 1

    # update output collections
    output_levels_lookup[level_index].append(left_node_index)
    output_levels_lookup[level_index].append(right_node_index)

    assert all([item not in output_node_by_index for item in (left_node_index, right_node_index)])
    output_node_by_index[left_node_index] = node.left
    output_node_by_index[right_node_index] = node.right

    next_level_index = level_index + 1
    if node.left is not None:
        traverse_level_order_v3_helper(
            node=node.left,
            level_index=next_level_index,
            parent_node_array_index=left_node_index,
            output_levels_lookup=output_levels_lookup,
            output_node_by_index=output_node_by_index,
        )

    if node.right is not None:
        traverse_level_order_v3_helper(
            node=node.right,
            level_index=next_level_index,
            parent_node_array_index=right_node_index,
            output_levels_lookup=output_levels_lookup,
            output_node_by_index=output_node_by_index,
        )




