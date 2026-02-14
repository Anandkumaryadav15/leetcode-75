from typing import List

class Solution:
    """
    Problem: House Robber II
    
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    
    Time Complexity: O(n)
    - We run the robust House Robber I solution twice, each taking O(n).
    
    Space Complexity: O(1)
    - Reusing constant space logic.
    """
    def rob(self, nums: List[int]) -> int:
        # Since houses are circular, we can't rob both first and last house.
        # So we try two scenarios:
        # 1. Rob houses from index 0 to n-2 (exclude last)
        # 2. Rob houses from index 1 to n-1 (exclude first)
        # Take the maximum of these two + handle edge case of single house.
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        # Standard House Robber logic
        rob1, rob2 = 0, 0
        
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
