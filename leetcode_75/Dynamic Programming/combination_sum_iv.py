from typing import List

class Solution:
    """
    Problem: Combination Sum IV
    
    Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
    The test cases are generated so that the answer can fit in a 32-bit integer.
    Note that different sequences are counted as different combinations (i.e., permutations matter).
    
    Time Complexity: O(target * n)
    - We calculate combinations for every value up to target, iterating through all nums each time.
    
    Space Complexity: O(target)
    - DP array of size target + 1.
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] = number of ways to get sum i
        dp = {0: 1}
        
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                # If we pick 'n' as the last number, ways(total) += ways(total - n)
                dp[total] += dp.get(total - n, 0)
                
        return dp[target]
