from linked_list.common_utils.conversions import convert_list_node_to_list, convert_list_to_list_node
from linked_list.common_utils.list_node import ListNode


def swap_pairs(head: ListNode | None) -> ListNode | None:
    if head is None:
        return None
    return None
    # return swap_pairs_helper(head)
    # return head


def reverse_helper(
        node_head: ListNode,
        k: int,
        node_curr: ListNode | None,
        k_curr: int,
) -> ListNode:
    if node_curr:
        return node_head
    if node_curr.next is None:
        return node_head

    if k_curr >= k:
        pass
    else:
        return reverse_helper(node_head, k, node_curr.next, k_curr + 1)

    # """
    # for k = 3
    # 1 -> 2 -> 3
    # becomes
    # 3 -> 2 -> 1
    # """
    # head_new = head_old.next
    # # head_old.next = head_new.next
    #
    # if head_new.next is None:
    #     head_old.next = None
    # else:
    #     head_old.next = swap_pairs_helper(head_old=head_new.next)
    #
    # head_new.next = head_old
    #
    # return head_new
    # # # 1 -> 3
    # # head.next = head.next.next
    # # # head is now: (val=2, next=3)
    # # head.next = head
    # # head_next = head.next
    # #
    # # head.next =


if __name__ == '__main__':
    head1 = convert_list_to_list_node([1, 2, 3, 4])
    output1 = swap_pairs(head1)
    output_as_list1 = convert_list_node_to_list(output1)
    print(output_as_list1)