from typing import List

class Solution:
    """
    Problem: Merge Intervals
    
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
    
    Time Complexity: O(n log n)
    - Sorting dominates the complexity.
    
    Space Complexity: O(n)
    - To store the output.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time is key
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            # If current start is <= last end, there is an overlap
            if start <= lastEnd:
                # Merge: end time becomes max of both end times
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap, just append
                output.append([start, end])
        return output
