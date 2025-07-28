import heapq

class MedianFinder:

    def __init__(self):
        # max heap for smaller half
        self.max_heap_for_lows = []
        heapq.heapify(self.max_heap_for_lows)

        # min heap for larger half
        # -> max len(lows) = len(highs) + 1
        self.min_heap_for_highs = []
        heapq.heapify(self.max_heap_for_lows)


    def addNum(self, num: int) -> None:
        # add to max heap
        self._max_heap_for_lows_push(num)

        # balancing step
        # -> b/c low received a new elt
        # --> remove largest elt from low and give it to high
        lows_top = self._max_heap_for_lows_pop_and_get_top()
        heapq.heappush(self.min_heap_for_highs, lows_top)

        # maintain size property (i.e. max len(lows) = len(highs) + 1)
        if len(self.max_heap_for_lows) < len(self.min_heap_for_highs):
            highs_top = heapq.heappop(self.min_heap_for_highs)
            self._max_heap_for_lows_push(highs_top)

    def findMedian(self) -> float:
        """
        if we have processed k elements:
        - If k=2∗n+1(∀n∈Z),
          - then lo is allowed to hold n+1 elements, while hi can hold n elements.
        - If k=2∗n(∀n∈Z),
          - then both heaps are balanced and hold n elements each.
        - This gives us the nice property that:
          - when the heaps are perfectly balanced,
          - the median can be derived from the tops of both heaps.
          - Otherwise, the top of the max-heap lo holds the legitimate median
        :return:
        """
        lows_top = self._max_heap_for_lows_get_top()
        if len(self.max_heap_for_lows) > len(self.min_heap_for_highs):
            return float(lows_top)
        else:
            highs_top = self.min_heap_for_highs[0]
            return (lows_top + highs_top) / 2.0

    def _max_heap_for_lows_get_top(self) -> int:
        return -self.max_heap_for_lows[0]

    def _max_heap_for_lows_pop_and_get_top(self) -> int:
        return -heapq.heappop(self.max_heap_for_lows)

    def _max_heap_for_lows_push(self, val: int) -> None:
        heapq.heappush(self.max_heap_for_lows, -val)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()