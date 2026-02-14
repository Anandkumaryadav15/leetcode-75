from typing import List

class Solution:
    """
    Problem: Missing Number
    
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    
    Time Complexity: O(n)
    - Summing takes O(n).
    
    Space Complexity: O(1)
    - Only constant extra space.
    """
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Calculate the expected sum of numbers from 0 to n.
        # Formula for sum of first n natural numbers is n * (n + 1) / 2
        expected_sum = n * (n + 1) // 2
        
        # Calculate the actual sum of elements in the array
        actual_sum = sum(nums)
        
        # The difference is the missing number
        return expected_sum - actual_sum
