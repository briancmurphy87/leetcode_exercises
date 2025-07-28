from linked_list.common_utils.list_node import ListNode


def convert_list_to_list_node_helper(
        list_of_ints: list[int],
        list_index: int,
) -> ListNode | None:
    if list_index >= len(list_of_ints):
        return None

    return ListNode(
        val=list_of_ints[list_index],
        next=convert_list_to_list_node_helper(list_of_ints, list_index + 1)
    )


def convert_list_to_list_node(
        list_of_ints: list[int],
) -> ListNode | None:
    if not list_of_ints:
        return None

    return convert_list_to_list_node_helper(list_of_ints, 0)


def convert_list_node_to_list(
        list_node: ListNode | None,
) -> list[int]:
    if not list_node:
        return []

    output: list[int] = [list_node.val]
    list_node_curr = list_node.next
    while list_node_curr is not None:
        output.append(list_node_curr.val)
        list_node_curr = list_node_curr.next

    return output
