def max_heapify(lst: list[int], heap_size: int, index: int) -> None:
    left, right = 2 * index + 1, 2 * index + 2
    largest = index
    if left < heap_size and lst[left] > lst[largest]:
        largest = left
    if right < heap_size and lst[right] > lst[largest]:
        largest = right
    if largest != index:
        lst[index], lst[largest] = lst[largest], lst[index]
        max_heapify(heap_size, largest)


class Solution:
    def heap_sort(self, lst: list[int]) -> None:
        """
        Mutates elements in lst by utilizing the heap data structure
        """
        # heapify original lst
        for i in range(len(lst) // 2 - 1, -1, -1):
            max_heapify(lst, len(lst), i)

        # use heap to sort elements
        for i in range(len(lst) - 1, 0, -1):
            # swap last element with first element
            lst[i], lst[0] = lst[0], lst[i]
            # note that we reduce the heap size by 1 every iteration
            max_heapify(lst, i, 0)