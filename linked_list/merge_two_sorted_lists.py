"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

"""
from linked_list.common_utils.conversions import convert_list_to_list_node, convert_list_node_to_list
from linked_list.common_utils.list_node import ListNode


def merge_two_lists(
    list1: ListNode | None,
    list2: ListNode | None,
) -> ListNode | None:
    # build initial output node
    next_list_info = get_next_list_to_pop(list1, list2)
    if next_list_info is None:
        return None

    next_list_selection, next_list_val = next_list_info

    output_list_node = ListNode(
        val=next_list_val,
    )
    if next_list_selection == 1:
        merge_two_lists_helper(
            list1=list1.next,
            list2=list2,
            output_list_node=output_list_node,
        )
    else:
        merge_two_lists_helper(
            list1=list1,
            list2=list2.next,
            output_list_node=output_list_node,
        )
    return output_list_node


def merge_two_lists_helper(
        list1: ListNode | None,
        list2: ListNode | None,
        output_list_node: ListNode,
) -> ListNode | None:
    assert output_list_node.next is None
    next_list_info = get_next_list_to_pop(list1, list2)
    if next_list_info is None:
        return None

    next_list_selection, next_list_val = next_list_info
    output_list_node.next = ListNode(
        val=next_list_val,
    )

    if next_list_selection == 1:
        merge_two_lists_helper(
            list1=list1.next,
            list2=list2,
            output_list_node=output_list_node.next,
        )
    else:
        merge_two_lists_helper(
            list1=list1,
            list2=list2.next,
            output_list_node=output_list_node.next,
        )

    return output_list_node

def get_next_list_to_pop(
    list1: ListNode | None,
    list2: ListNode | None,
) -> tuple[int, int] | None:

    l1_val: int | None = list1.val if list1 else None
    l2_val: int | None = list2.val if list2 else None
    if l1_val is None and l2_val is None:
        return None

    elif l1_val is None:
        return 2, l2_val

    elif l2_val is None:
        return 1, l1_val

    elif l2_val < l1_val:
        # return l2_val
        return 2, l2_val

    else:
        # l1_val <= l1_val
        return 1, l1_val


if __name__ == '__main__':
    """
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]
    """
    # list1 = convert_list_to_list_node([1, 2, 4])
    # list2 = convert_list_to_list_node([1, 3, 4])
    list1 = convert_list_to_list_node([])
    list2 = convert_list_to_list_node([0])

    merged_list_node1 = merge_two_lists(list1, list2)
    merged_list1 = convert_list_node_to_list(merged_list_node1)
    print(merged_list1)
