import heapq

class MedianFinder:
    """
    Problem: Find Median from Data Stream
    
    The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
    Implement the MedianFinder class:
    - MedianFinder() initializes the MedianFinder object.
    - void addNum(int num) adds the integer num from the data stream to the data structure.
    - double findMedian() returns the median of all elements so far.
    
    Time Complexity:
    - addNum: O(log n)
    - findMedian: O(1)
    
    Space Complexity: O(n)
    - Storing all numbers in two heaps.
    """

    def __init__(self):
        # We use two heaps:
        # small: a Max-Heap to store the smaller half of the numbers
        # large: a Min-Heap to store the larger half of the numbers
        # By default Python has Min-Heap. Multiply by -1 to simulate Max-Heap.
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # 1. Add to small (max-heap)
        heapq.heappush(self.small, -1 * num)
        
        # 2. Ensure every element in small is <= every element in large
        if (self.small and self.large and
            (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Handle uneven size (small can be equal or 1 size greater than large)
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If one heap is larger, the median is its root
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
            
        # If equal size, average of roots
        return (-1 * self.small[0] + self.large[0]) / 2.0
