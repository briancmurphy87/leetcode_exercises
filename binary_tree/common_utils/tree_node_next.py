from typing import Optional


class Node:
    def __init__(
            self,
            val: int=0,
            left: Optional["Node"] = None,
            right: Optional["Node"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

        self.next: Optional["Node"] = None
