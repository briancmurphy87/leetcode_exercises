from binary_tree.common_utils.tree_node import TreeNode


def traverse_pre_order_recursive(
        root: TreeNode | None,
        output: list[int],
) -> None:

    if root is None:
        return

    output.append(root.val)
    traverse_pre_order_recursive(root.left, output)
    traverse_pre_order_recursive(root.right, output)


def traverse_pre_order(root: TreeNode) -> list[int]:
    output: list[int] = []
    traverse_pre_order_recursive(root, output)
    return output

def traverse_pre_order_with_stack(root: TreeNode) -> list[int]:
    output: list[int] = []

    stack: list[TreeNode] = []
    if root is not None:
        stack.append(root)

    while stack:
        node_curr: TreeNode = stack.pop()

        # visit the ROOT
        output.append(node_curr.val)

        # push RIGHT child to stack if it is not null
        if node_curr.right is not None:
            stack.append(node_curr.right)

        # push LEFT child to stack if it is not null
        if node_curr.left is not None:
            stack.append(node_curr.left)

    return output