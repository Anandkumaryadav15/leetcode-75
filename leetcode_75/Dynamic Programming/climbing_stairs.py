class Solution:
    """
    Problem: Climbing Stairs
    
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    Time Complexity: O(n)
    - We calculate the value for each step once.
    
    Space Complexity: O(1)
    - We only store the previous two values, so we optimize space from O(n) to O(1).
    """
    def climbStairs(self, n: int) -> int:
        # Base case: if n is small, return n immediately
        if n <= 2:
            return n
        
        # Determine the ways to reach step 1 and step 2
        one, two = 1, 1
        
        # Iterate from 2 to n (shifted slightly in loop logic)
        for i in range(n - 1):
            temp = one
            one = one + two # New value is sum of previous two (Fibonacci)
            two = temp      # Move the window
            
        return one
