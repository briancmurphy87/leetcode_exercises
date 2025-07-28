from binary_tree.common_utils.tree_node import TreeNode


def traverse_post_order_recursive(
        root: TreeNode | None,
        output: list[int],
) -> None:
    if root is None:
        return

    # traverse subtree to LEFT
    traverse_post_order_recursive(root.left, output)
    # traverse subtree to RIGHT
    traverse_post_order_recursive(root.right, output)
    # visit the ROOT
    output.append(root.val)

def traverse_post_order(root: TreeNode) -> list[int]:
    output: list[int] = []
    traverse_post_order_recursive(root, output)
    return output
