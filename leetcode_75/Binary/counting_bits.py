from typing import List

class Solution:
    """
    Problem: Counting Bits
    
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
    
    Time Complexity: O(n)
    - Single pass through numbers from 0 to n.
    
    Space Complexity: O(1)
    - Ignoring the output array.
    """
    def countBits(self, n: int) -> List[int]:
        # Initialize result array of size n+1 with 0s
        ans = [0] * (n + 1)
        
        # Iterate from 1 to n to fill the array
        for i in range(1, n + 1):
            # ans[i >> 1] represents the number of set bits in i // 2.
            # (i & 1) adds 1 if the last bit is set (i.e., i is odd).
            # Example:
            # i = 5 (101), i >> 1 = 2 (10). ans[5] = ans[2] + 1
            # i = 4 (100), i >> 1 = 2 (10). ans[4] = ans[2] + 0
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans
