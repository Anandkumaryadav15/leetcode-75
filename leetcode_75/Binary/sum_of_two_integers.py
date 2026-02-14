class Solution:
    """
    Problem: Sum of Two Integers
    
    Given two integers a and b, return the sum of the two integers without using the operators + and -.
    
    Time Complexity: O(1)
    - In languages with fixed-width integers (like Java/C++), this runs in constant time (32 iterations max).
    - In Python, due to arbitrary precision integers, we simulate 32-bit behavior. The loop runs until carry is 0.
    
    Space Complexity: O(1)
    - Constant extra space.
    """
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to restrict operations to 32 bits
        # Python handles large integers automatically, so we need to manually clamp to 32 bits
        mask = 0xFFFFFFFF
        
        while b != 0:
            # a ^ b gives the sum without carry (XOR)
            # (a & b) << 1 gives the carry (AND shifted left)
            # We want to continue adding the carry until there is no carry left.
            
            tmp = (a ^ b) & mask    # Sum without carry
            carry = ((a & b) << 1) & mask # Carry calculation
            
            a = tmp
            b = carry
            
        # If a is a negative number in 32-bit representation (starts with 1 in 32nd bit)
        # We need to convert it back to Python's negative integer format
        # 0x7FFFFFFF is the max positive 32-bit integer
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
            
        return a
