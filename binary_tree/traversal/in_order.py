from binary_tree.common_utils.tree_node import TreeNode


def traverse_in_order_recursive(
        root: TreeNode | None,
        output: list[int],
) -> None:

    if root is None:
        return
    # traverse subtree to LEFT
    traverse_in_order_recursive(root.left, output)
    # visit the ROOT
    output.append(root.val)
    # traverse subtree to RIGHT
    traverse_in_order_recursive(root.right, output)


def traverse_in_order(root: TreeNode) -> list[int]:
    output: list[int] = []
    traverse_in_order_recursive(root, output)
    return output
