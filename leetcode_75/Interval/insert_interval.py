from typing import List

class Solution:
    """
    Problem: Insert Interval
    
    You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
    You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
    Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    Return intervals after the insertion.
    
    Time Complexity: O(n)
    - Single pass to iterate through intervals.
    
    Space Complexity: O(n)
    - To store the result list.
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            # If new interval is strictly before the current interval, it fits here.
            # Since the list is sorted, all subsequent intervals are also after.
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # If new interval is strictly after the current interval, 
            # we just append the current one and keep checking where newInterval fits.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # If there is an overlap, merge them.
            # We don't append yet because the merged interval might overlap with the next one too.
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])]
        
        # Append the (possibly merged) newInterval if it hasn't been added
        res.append(newInterval)
        return res
