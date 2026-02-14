from typing import List

class Solution:
    """
    Problem: Longest Consecutive Sequence
    
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.
    
    Time Complexity: O(n)
    - We iterate through the array once to build the set.
    - We iterate again, but the inner while loop only runs for the beginning of sequences. Each element is visited at most twice.
    
    Space Complexity: O(n)
    - To store the set.
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            # Check if it's the start of a sequence
            # If (n - 1) is in the set, then n is not the start, so we skip it.
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
                
        return longest
