from binary_tree.common_utils.get_index import get_child_index_left, get_child_index_right
from binary_tree.common_utils.tree_node import TreeNode

TreeArrayElement = int | None

def create_binary_tree_array_from_root_node_helper(
    root_node: TreeNode | None,
    root_node_index: int,
    output_tree_index_to_element: dict[int, TreeArrayElement],
) -> None:
    assert root_node_index not in output_tree_index_to_element

    root_node_value: TreeArrayElement = None if root_node is None else root_node.val
    output_tree_index_to_element[root_node_index] = root_node_value

def create_binary_tree_array_from_root_node_impl(
    root_node: TreeNode | None,
    root_node_index: int,
    output_tree_index_to_element: dict[int, TreeArrayElement],
) -> None:
    # add ROOT
    create_binary_tree_array_from_root_node_helper(
        root_node=root_node,
        root_node_index=root_node_index,
        output_tree_index_to_element=output_tree_index_to_element,
    )
    # hit leaf? stop adding elements to array for this subtree
    root_node_is_leaf = root_node is None or (root_node.left is None and root_node.right is None)
    if root_node_is_leaf:
        return

    # add child to LEFT + RIGHT
    child_nodes_tuple2: tuple[TreeNode | None, TreeNode | None]
    if root_node is None:
        child_nodes_tuple2 = None, None
    else:
        child_nodes_tuple2 = root_node.left, root_node.right

    for child_node_index, child_node in zip(
            (
                get_child_index_left(root_node_index),
                get_child_index_right(root_node_index),
            ),
            child_nodes_tuple2,
    ):
        create_binary_tree_array_from_root_node_impl(
            root_node=child_node,
            root_node_index=child_node_index,
            output_tree_index_to_element=output_tree_index_to_element,
        )


def create_binary_tree_array_from_root_node(
    root_node: TreeNode | None,
    # tree_array: list[TreeArrayElement],
) -> list[TreeArrayElement]:
    if root_node is None:
        return []

    # init output lookup
    output_tree_index_to_element: dict[int, TreeArrayElement] = {}

    create_binary_tree_array_from_root_node_impl(
        root_node=root_node,
        root_node_index=0,
        output_tree_index_to_element=output_tree_index_to_element,
    )

    out_node_index_max = max(output_tree_index_to_element.keys())

    # convert to output list + return
    output_tree_array_len = out_node_index_max + 1
    output_tree_array: list[TreeArrayElement] = [None] * output_tree_array_len
    for out_node_index in range(0, out_node_index_max + 1):
        # assert out_node_index in output_tree_index_to_element, out_node_index
        output_tree_element = output_tree_index_to_element.get(out_node_index, None)
        if output_tree_element is not None:
            output_tree_array[out_node_index] = output_tree_element

    return output_tree_array