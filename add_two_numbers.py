class ListNode:
    def __init__(self, val: int=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

    out_head = ListNode(val=l1.val + l2.val)
    out_tail = addTwoNumbersStep(l1.next, l2.next, out_head)
    return out_head


def addTwoNumbersStep(l1: ListNode | None, l2: ListNode | None, curr_out_node: ListNode | None, remainder: bool = False) -> ListNode | None:
    l1_is_none = l1 is None
    l2_is_none = l2 is None
    if l1_is_none and l2_is_none:
        return None
    elif l1_is_none:
        return l2
    elif l2_is_none:
        return l2
    else:


        new_val = l1.val + l2.val
        assert 0 < new_val < 20
        if new_val >= 10:
            new_val_rem = True
            new_val_final = new_val - 10
        else:
            new_val_rem = False
            new_val_final = new_val


        curr_out_node.next = ListNode(val=new_val_final)
        return addTwoNumbersStep(l1.next, l2.next, curr_out_node.next, new_val_rem)



    #
    #
    #     return ListNode(val=l1.val + l2.val, next=addTwoNumbersStep(l1.next, l2.next, curr_out_node))
    #
    # output: list[ListNode] = []
    #
    # l1_node = l1[0]
    # l2_node = l2[0]
    # while not (l1_node.next is None and l2_node.next is None):
    #     l1_val = 0 if l1.


if __name__ == '__main__':
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

    res = addTwoNumbers(l1, l2)
    assert isinstance(res, ListNode)

    iter = 0
    res_iter = res
    while res_iter.next is not None:
        print(f"|res.val={res_iter.val} |iter={iter}")
        iter+=1