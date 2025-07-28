from collections import defaultdict

from binary_tree.common_utils.init_bt_from_array import create_binary_tree_from_array
from binary_tree.common_utils.tree_node_next import Node
from binary_tree.traversal.level_order_v3 import TraverseLevelOrderOutput, traverse_level_order_v3


class PopulateNextRightPointersOutput:
    def __init__(
            self,
            level_order_traverse_output: TraverseLevelOrderOutput,
            revised_tree_array_index_to_node: defaultdict[int, Node | None],
    ) -> None:
        self.level_order_traverse_output = level_order_traverse_output
        self.revised_tree_array_index_to_node = revised_tree_array_index_to_node


def populate_next_right_pointers_impl(
        root: Node | None,
) -> PopulateNextRightPointersOutput | None:
    if root is None:
        return None

    # TODO: filter down to what you need
    traverse_level_output: TraverseLevelOrderOutput = traverse_level_order_v3(root_node=root)
    revised_tree_array_index_to_node: defaultdict[int, Node | None] = traverse_level_output.tree_array_index_to_node

    for level_index, level_node_array_indices in traverse_level_output.level_index_to_level_node_indices.items():
        # traverse nodes at this level from right to left
        for lhs_node_index_within_level in range(len(level_node_array_indices) - 2, -1, -1):
            # get LEFT node
            lhs_node: Node | None = traverse_level_output.tree_array_index_to_node[
                    level_node_array_indices[lhs_node_index_within_level]
                ]
            if lhs_node is None:
                continue

            # get RIGHT node (jumping over the null children where necessary)
            rhs_node: Node | None = None
            rhs_node_index_within_level = lhs_node_index_within_level + 1
            while rhs_node_index_within_level < len(level_node_array_indices) and rhs_node is None:
                # get candidate right-hand-side node
                rhs_node = traverse_level_output.tree_array_index_to_node[
                    level_node_array_indices[rhs_node_index_within_level]
                ]
                # increment for next pass
                rhs_node_index_within_level += 1

            if rhs_node is None:
                continue

            # set 'next' attribute for 'next-right pointer' of left-hand-side node
            assert lhs_node.next is None
            lhs_node.next = rhs_node

    return PopulateNextRightPointersOutput(
        level_order_traverse_output=traverse_level_output,
        revised_tree_array_index_to_node=revised_tree_array_index_to_node,
    )

def populate_next_right_pointers(root: Node | None) -> Node | None:
    output: PopulateNextRightPointersOutput | None = (
        populate_next_right_pointers_impl(root=root)
    )
    if output is None:
        return None

    # return root-level node
    return output.revised_tree_array_index_to_node[0]


def pretty_print_output(output: PopulateNextRightPointersOutput) -> None:
    traverse_output = output.level_order_traverse_output
    max_node_index = max(traverse_output.tree_array_index_to_node.keys())
    for node_index in range(0, max_node_index + 1):
        node = traverse_output.tree_array_index_to_node[node_index]
        fmt_node = "None" if node is None else f"[val={node.val}; next_is_none={str(node.next is None)}]"
        print(f"|node_index={str(node_index).rjust(2, '0')} node: {fmt_node}")


if __name__ == '__main__':
    tree_array2 = [1, 2, 3, 4, 5, None, 7]
    output2: PopulateNextRightPointersOutput | None = (
        populate_next_right_pointers_impl(
            create_binary_tree_from_array(tree_array2)
        )
    )
    pretty_print_output(output2)

    # tree_array1 = [1, 2, 3, 4, 5, 6, 7]
    # tree_root_node1 = create_binary_tree_from_array(tree_array1)
    # output1: PopulateNextRightPointersOutput | None = populate_next_right_pointers_impl(tree_root_node1)
    # pretty_print_output(output1)


    x =0
    # # TODO: filter down to what you need
    # output_levels, output_levels_lookup, output_node_by_index = traversal_output1

