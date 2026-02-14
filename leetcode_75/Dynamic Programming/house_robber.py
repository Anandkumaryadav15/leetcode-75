from typing import List

class Solution:
    """
    Problem: House Robber
    
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    
    Time Complexity: O(n)
    - Single pass through the houses.
    
    Space Complexity: O(1)
    - We only store the max loot of the previous two houses implicitly.
    """
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # At each house n, we decide:
            # 1. Skip n: We keep the loot up to rob2.
            # 2. Rob n: We add n to loot from rob1 (previous-previous house).
            temp = max(n + rob1, rob2)
            
            # Shift our window
            rob1 = rob2
            rob2 = temp
            
        return rob2
