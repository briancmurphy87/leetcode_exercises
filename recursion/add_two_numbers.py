"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

"""
from linked_list.common_utils.conversions import convert_list_to_list_node, convert_list_node_to_list


class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    return add_two_numbers_step(
        lhs=l1,
        rhs=l2,
        carry_over=False,
    )

def add_two_numbers_step(
        lhs: ListNode | None,
        rhs: ListNode | None,
        carry_over: bool,
) -> ListNode | None:
    if lhs is None and rhs is None:
        if carry_over:
            return ListNode(val=1, next=None)
        else:
            return None

    lhs_val = lhs.val if lhs is not None else 0
    rhs_val = rhs.val if rhs is not None else 0
    new_val = lhs_val + rhs_val
    if carry_over:
        new_val += 1

    lhs_next = None if lhs is None else lhs.next
    rhs_next = None if rhs is None else rhs.next
    if new_val >= 10:
        return ListNode(
            val=(new_val - 10),
            next=add_two_numbers_step(
                lhs=lhs_next,
                rhs=rhs_next,
                carry_over=True,
            ),
        )
    else:
        return ListNode(
            val=new_val,
            next=add_two_numbers_step(
                lhs=lhs_next,
                rhs=rhs_next,
                carry_over=False,
            ),
        )

if __name__ == '__main__':

    out1 = add_two_numbers(
        l1=convert_list_to_list_node([9,9,9,9,9,9,9]
),
        l2=convert_list_to_list_node([9,9,9,9]),
    )
    out1_list = convert_list_node_to_list(out1)
    print(out1_list)
    """
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    Example 2:
    
    Input: l1 = [0], l2 = [0]
    Output: [0]
    Example 3:
    
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
    """