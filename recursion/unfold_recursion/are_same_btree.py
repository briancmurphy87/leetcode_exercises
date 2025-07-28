from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int=0,
        left=Optional["TreeNode"],
        right=Optional["TreeNode"],
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        # p and q are both None
        if not p and not q:
            return True

        # one of p and q is None
        if not q or not p:
            return False

        if p.val != q.val:
            return False

        return (
                self.isSameTree(p.right, q.right)
                and  self.isSameTree(p.left, q.left)
        )

def is_same_tree_iteration(p: TreeNode, q: TreeNode) -> bool:
    def check(p: TreeNode, q: TreeNode) -> bool:
        # if both are None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return True

    deq = deque([(p, q), ])
    while deq:
        p, q = deq.popleft()
        if not check(p, q):
            return False
        if p:
            deq.append((p.left, q.left))
            deq.append((p.right, q.right))
            
    return True