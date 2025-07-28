from binary_tree.common_utils.get_index import get_child_index_left, get_child_index_right
from binary_tree.common_utils.tree_node import TreeNode


def create_binary_tree_from_array_impl(
        tree_array: list[int | None],
        tree_array_len: int,
        node_root_index: int,
        other_nodes_returned: dict[int, TreeNode | None],
        other_nodes_returned_indices: frozenset[int],
) -> TreeNode | None:
    node_root_value: int | None = (
        None
        if node_root_index >= tree_array_len
        else tree_array[node_root_index]
    )

    node_to_be_returned = node_root_index in other_nodes_returned_indices
    assert node_root_index not in other_nodes_returned

    if node_root_value is None:
        if node_to_be_returned:
            other_nodes_returned[node_root_index] = None
        return None

    # # add root node
    # output_node_array.append(
    #     TreeNodeWithIndex(
    #         node_array_index=node_root_index,
    #         val=node_root_value,
    #     )
    # )

    # then add child nodes
    node_index_left, node_index_right = [
        get_child_index(node_root_index)
        for get_child_index in (get_child_index_left, get_child_index_right)
    ]

    new_node = TreeNode(
        # node_array_index=node_root_index,
        val=node_root_value,
        left=create_binary_tree_from_array_impl(
            tree_array=tree_array,
            tree_array_len=tree_array_len,
            node_root_index=node_index_left,
            other_nodes_returned=other_nodes_returned,
            other_nodes_returned_indices=other_nodes_returned_indices,
        ),
        right=create_binary_tree_from_array_impl(
            tree_array=tree_array,
            tree_array_len=tree_array_len,
            node_root_index=node_index_right,
            other_nodes_returned=other_nodes_returned,
            other_nodes_returned_indices=other_nodes_returned_indices,
        ),
    )
    if node_to_be_returned:
        other_nodes_returned[node_root_index] = new_node

    return new_node


def create_binary_tree_from_array(
    tree_array: list[int | None],
    other_nodes_returned_indices: frozenset[int] = frozenset({}),
) -> tuple[TreeNode | None, dict[int, TreeNode | None]]:
    if not tree_array:
        return None, {}

    other_nodes_returned: dict[int, TreeNode | None] = {}
    root_node = create_binary_tree_from_array_impl(
        tree_array=tree_array,
        tree_array_len=len(tree_array),
        node_root_index=0,
        other_nodes_returned=other_nodes_returned,
        other_nodes_returned_indices=other_nodes_returned_indices,
    )
    return root_node, other_nodes_returned