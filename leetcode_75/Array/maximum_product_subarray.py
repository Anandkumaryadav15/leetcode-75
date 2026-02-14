from typing import List

class Solution:
    """
    Problem: Maximum Product Subarray
    
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
    The test cases are generated so that the answer will fit in a 32-bit integer.
    
    Time Complexity: O(n)
    - Single pass through the array.
    
    Space Complexity: O(1)
    - We only store a few variables for max/min so far.
    """
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # We need to keep track of both min and max product because a negative number 
        # multiplied by a negative minimum can become a large maximum.
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # Since we are modifying max_so_far, we need to save it for the min_so_far calculation
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            
            max_so_far = temp_max
            
            # Update the global result
            result = max(max_so_far, result)
            
        return result
