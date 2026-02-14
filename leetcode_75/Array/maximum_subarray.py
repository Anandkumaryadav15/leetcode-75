from typing import List

class Solution:
    """
    Problem: Maximum Subarray
    
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    
    Time Complexity: O(n)
    - We iterate through the array once.
    
    Space Complexity: O(1)
    - We only use a couple of variables.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Initialize current_sum and max_sum with the first element
        current_sum = nums[0]
        max_sum = nums[0]
        
        # Iterate from the second element
        for i in range(1, len(nums)):
            # Kadane's Algorithm:
            # At each step, we decide whether to start a new subarray at nums[i]
            # or extend the existing subarray.
            # If current_sum + nums[i] < nums[i], it means the previous subarray was dragging us down,
            # so we start fresh at nums[i].
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update global max
            max_sum = max(max_sum, current_sum)
            
        return max_sum
