from typing import List

class Solution:
    """
    Problem: Non-overlapping Intervals
    
    Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    
    Time Complexity: O(n log n)
    - Sorting takes most time.
    
    Space Complexity: O(1)
    - Assuming in-place sort or ignoring sort space.
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by end time to maximize the number of non-overlapping intervals we can keep
        # Greedy approach: always pick the interval that ends earliest to leave room for others
        intervals.sort(key=lambda x: x[1])
        res = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            # If current start is >= previous end, no overlap
            if start >= prevEnd:
                prevEnd = end
            else:
                # Overlap detected, we "remove" the current interval (increment count)
                # We keep the one with smaller end time (which is prevEnd, since we sorted by end time,
                # but actually here we just don't update prevEnd - effectively keeping the previous one)
                # Wait, strictly speaking sorting by end time means prevEnd <= end.
                # So we keep the previous one (which ends earlier) and discard current.
                res += 1
                
        return res
