from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    Problem: Meeting Rooms
    
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
    
    Time Complexity: O(n log n)
    - Sorting.
    
    Space Complexity: O(1)
    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i: i[0])
        
        for i in range(len(intervals) - 1):
            # If current meeting ends after next meeting starts, overlap exists
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
