from collections import defaultdict


class TwoSum:

    def __init__(self):
        self._vals: list[int] = []
        self._is_sorted = False
        # self._val_to_indices: defaultdict[int, list[int]] = defaultdict(list)

    def add(self, number: int) -> None:
        new_index = len(self._vals)
        self._vals.append(number)
        self._is_sorted = False
        # self._val_to_indices[number].append(new_index)

    def find(self, value: int) -> bool:
        if not self._is_sorted:
            self._vals.sort()
            self._is_sorted = True

        low, high = 0, len(self._vals) - 1
        while low < high:
            curr_sum = self._vals[low] + self._vals[high]
            if curr_sum < value:
                low += 1
            elif curr_sum > value:
                high -= 1
            else:
                return True
        return False