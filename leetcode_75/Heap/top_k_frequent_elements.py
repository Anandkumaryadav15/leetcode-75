from typing import List
import heapq

class Solution:
    """
    Problem: Top K Frequent Elements
    
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
    
    Time Complexity: O(n log k)
    - Counting takes O(n).
    - Heap operations take O(n log k) if we keep heap size at k.
    
    Space Complexity: O(n + k)
    - Hash map stores n unique elements. Heap stores k elements.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Min-heap to store the top k elements
        # We store (frequency, num) so heap is ordered by frequency
        heap = []   
        for n in count:
            heapq.heappush(heap, (count[n], n))
            # If heap size exceeds k, pop minimum
            # The smallest frequency elements will be removed, leaving only the largest frequency elements
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
