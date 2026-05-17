import heapq

class MedianFinder:

    def __init__(self):
        # max heap (left half)
        self.small = []
        # min heap (right half)
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: add to max heap (invert sign for max heap behavior)
        heapq.heappush(self.small, -num)

        # Step 2: balance - ensure every element in small <= every element in large
        if (self.small and self.large and
                (-self.small[0] > self.large[0])):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: balance sizes (small can have at most 1 extra element)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If odd number of elements
        if len(self.small) > len(self.large):
            return -self.small[0]

        # If even number of elements
        return (-self.small[0] + self.large[0]) / 2.0