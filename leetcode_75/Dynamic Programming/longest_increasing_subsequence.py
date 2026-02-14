from typing import List

class Solution:
    """
    Problem: Longest Increasing Subsequence
    
    Given an integer array nums, return the length of the longest strictly increasing subsequence.
    
    Time Complexity: O(n^2)
    - Nested loops: for every element i, we check all previous elements j.
    
    Space Complexity: O(n)
    - To store the DP array.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] represents the length of the longest increasing subsequence starting at index i
        LIS = [1] * len(nums)
        
        # Iterate backwards from the last element
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements that come after i
            for j in range(i + 1, len(nums)):
                # If nums[i] < nums[j], we can extend the LIS starting at j
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    
        return max(LIS)
