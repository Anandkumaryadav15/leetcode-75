from typing import List

class Solution:
    """
    Problem: Meeting Rooms II
    
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
    
    Time Complexity: O(n log n)
    - Sorting start and end times.
    
    Space Complexity: O(n)
    - To store sorted arrays.
    """
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        res, count = 0, 0
        s, e = 0, 0
        
        # Iterate through start times
        while s < len(intervals):
            # If a meeting starts before the earliest ending meeting ends, we need a new room
            if start[s] < end[e]:
                s += 1
                count += 1
            # If a meeting starts after (or when) a meeting ends, a room frees up
            else:
                e += 1
                count -= 1
            res = max(res, count)
            
        return res
