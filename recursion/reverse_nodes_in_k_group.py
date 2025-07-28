from typing import NamedTuple

from linked_list.common_utils.conversions import convert_list_node_to_list, convert_list_to_list_node
from linked_list.common_utils.list_node import ListNode


class ReverseNodesOutput: #(NamedTuple):
    def __init__(
            self,
            node_head_new: ListNode,
            node_post_k_seq: ListNode | None,
    ) -> None:
        self.node_head_new = node_head_new
        self.node_post_k_seq = node_post_k_seq

def reverse_k_group(head: ListNode | None, k: int) -> ListNode | None:
    if head is None:
        return None

    node_post_reverse_head_base, node_post_k_sequence_base = (
        reverse_k_group_helper(head=head, k=k, skip=0)
    )
    skip = k

    node_post_k_sequence = node_post_k_sequence_base
    while node_post_k_sequence is not None:
        node_post_reverse_head_iter, node_post_k_sequence = (
            reverse_k_group_helper(head=node_post_reverse_head_base, k=k, skip=skip)
        )
        skip += k
        x = 0
    return node_post_reverse_head_base

def reverse_k_group_helper(
        head: ListNode | None,
        k: int,
        skip: int,
) -> tuple[ListNode | None, ListNode | None]:

    if head is None:
        return None, None

    # nullify head node to avoid cycles
    node_old_head_next = head.next
    head.next = None

    # do recursion
    reverse_nodes_output = do_reverse_helper(
        k=k,
        k_curr=2,
        node_curr=node_old_head_next,
        node_prev=head,
        skip=skip,
        skip_curr=0,
    )
    # cannot reverse -> revert changes
    if reverse_nodes_output is None:
        head.next = node_old_head_next
        return head, None

    # point old head at node that comes after just-reversed k-sequence
    head.next = reverse_nodes_output.node_post_k_seq

    # return the new head
    # can_continue_reversing = reverse_nodes_output.node_post_k_seq is not None
    return (
        # can_continue_reversing,
        reverse_nodes_output.node_head_new,
        reverse_nodes_output.node_post_k_seq,
    )

def do_reverse_helper(
    k: int,
    k_curr: int,
    node_curr: ListNode | None,
    node_prev: ListNode,
    skip: int,
    skip_curr: int,
) -> ReverseNodesOutput | None:
    if node_curr is None:
        return None

    if k_curr >= k:
        # start to reverse pointers
        # -> return the next node just-outside the k-sequence
        node_post_k_seq = node_curr.next
        node_curr.next = node_prev
        return ReverseNodesOutput(
            node_head_new=node_curr,
            node_post_k_seq=node_post_k_seq,
        )

    # skip this node?
    next_skip_curr = (skip_curr + 1) if skip_curr < skip else skip_curr
    reverse_nodes_output = do_reverse_helper(
        k=k,
        k_curr=k_curr + 1,
        node_curr=node_curr.next,
        node_prev=node_curr,
        skip=skip,
        skip_curr=skip_curr,
    )
    if not (skip_curr > 0):
        node_curr.next = node_prev
    return reverse_nodes_output


if __name__ == '__main__':
    k1 = 2
    head1 = convert_list_to_list_node([1,2,3,4,5])
    output1 = reverse_k_group(head1, k1)
    output_as_list1 = convert_list_node_to_list(output1)
    print(output_as_list1)