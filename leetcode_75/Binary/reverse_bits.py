class Solution:
    """
    Problem: Reverse Bits
    
    Reverse bits of a given 32 bits unsigned integer.
    
    Time Complexity: O(1)
    - We iterate exactly 32 times.
    
    Space Complexity: O(1)
    - Constant space used.
    """
    def reverseBits(self, n: int) -> int:
        res = 0
        
        # Iterate through all 32 bits
        for i in range(32):
            # Get the i-th bit from n
            bit = (n >> i) & 1
            
            # Place that bit in the (31 - i) position in res
            # (31 - i) because we are reversing:
            # 0th bit goes to 31st
            # 1st bit goes to 30th etc.
            res = res | (bit << (31 - i))
            
        return res
