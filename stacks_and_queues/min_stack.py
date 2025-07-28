class MinStack:

    def __init__(self):
        self._stack: list[int] = []
        self._min_elt_state: int | None = None

        self._stack_vals_and_mins: list[tuple[int, int]] = []

    # def push(self, val: int) -> None:
        # # insert elt into stack
        # self._stack.append(val)
        #
        # if self._min_elt_state is None:
        #     self._min_elt_state = val
        # elif val < self._min_elt_state:
        #     self._min_elt_state = val

    def push(self, x: int) -> None:
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self._stack_vals_and_mins:
            self._stack_vals_and_mins.append((x, x))
            return
        current_min = self._stack_vals_and_mins[-1][1]
        self._stack_vals_and_mins.append((x, min(x, current_min)))

    def pop(self) -> None:
        self._stack_vals_and_mins.pop()
        # # delete element from queue -> return 'T' if successful
        # if not self._stack:
        #     return False
        #
        # deleted_val = self._stack.pop()
        # if deleted_val == self._min_elt_state:
        #     if not self._stack:
        #         self._min_elt_state = None
        #     else:
        #         self._min_elt_state = min(self._stack)
        #
        # return True

    def top(self) -> int:
        return self._stack_vals_and_mins[-1][0]
        # return self._stack[-1]

    def getMin(self) -> int:
        return self._stack_vals_and_mins[-1][1]
        # if self._min_elt_state is None:
        #     raise ValueError("stack is empty")
        # return self._min_elt_state

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    pass