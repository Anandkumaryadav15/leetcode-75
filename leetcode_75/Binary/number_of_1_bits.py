class Solution:
    """
    Problem: Number of 1 Bits
    
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
    
    Time Complexity: O(1)
    - Specifically, O(k) where k is the number of set bits. Since input is 32-bit, max k is 32.
    
    Space Complexity: O(1)
    - No extra space used.
    """
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # n & (n - 1) drops the lowest set bit.
            # Example:
            # n     = 1100 (12)
            # n-1   = 1011 (11)
            # n&(n-1) = 1000 (8) -> One bit removed
            n &= (n - 1)
            count += 1
        return count
