class MyCircularQueue:

    def __init__(self, k: int):
        self._queue_array: list[int | None] = [None] * k
        self._queue_array_len: int = k
        self._head_and_tail: tuple[int, int] | None = None

    def enqueue(self, value: int) -> bool:

        if self._head_and_tail is None:
            is_full = False
            head_index = 0
            tail_index_next = 0
        else:
            head_index, tail_index = self._head_and_tail
            is_full, tail_index_next = is_full_impl(head_index, tail_index, self._queue_array_len)

        if is_full:
            return False

        # add to array
        self._queue_array[tail_index_next] = value

        # update indices
        self._head_and_tail = (head_index, tail_index_next)

        return True

    def dequeue(self) -> bool:
        # is empty?
        if self._head_and_tail is None:
            return False

        head_index, tail_index = self._head_and_tail
        head_index_next = _get_incremented_index(array_index=head_index, k=self._queue_array_len)

        # remove element at old 'head' position
        self._queue_array[head_index] = None

        # update head/tail indices
        if head_index == tail_index:
            # is empty after delete?
            self._head_and_tail = None
        else:
            self._head_and_tail = (head_index_next, tail_index)

        return True

    def front(self) -> int:
        return -1 if self.is_empty() else self._queue_array[self._head_and_tail[0]]

    def rear(self) -> int:
        return -1 if self.is_empty() else self._queue_array[self._head_and_tail[1]]

    def is_empty(self) -> bool:
        return self._head_and_tail is None

    def is_full(self) -> bool:
        if self._head_and_tail is None:
            return False

        head_index, tail_index = self._head_and_tail
        is_full, _ = is_full_impl(head_index, tail_index, self._queue_array_len)
        return is_full

    def enQueue(self, value: int) -> bool:
        return self.enqueue(value)

    def deQueue(self) -> bool:
        return self.dequeue()

    def Front(self) -> int:
        return self.front()

    def Rear(self) -> int:
        return self.rear()

    def isEmpty(self) -> bool:
        return self.is_empty()

    def isFull(self) -> bool:
        return self.is_full()

def is_full_impl(head_index: int, tail_index: int, k: int) -> tuple[bool, int]:
    # head_index, tail_index = self._head_and_tail
    tail_next = _get_incremented_index(array_index=tail_index, k=k)
    return tail_next == head_index, tail_next

def _get_incremented_index(array_index: int, k: int) -> int:
    return (array_index + 1) % k


if __name__ == '__main__':
    ops = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    vals = [[3], [1], [2], [3], [4], [], [], [], [4], []]

    container = MyCircularQueue(k=vals[0][0])
    for op, val in zip(ops[1:], vals[1:]):
        if not val:
            result = getattr(container, op)()
        else:
            assert len(val) == 1
            result = getattr(container, op)(val[0])
        print(f"|result={result} |op={op} |val={val}")