class Solution:
    """
    Problem: Decode Ways
    
    A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1", 'B' -> "2", ... 'Z' -> "26".
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (s).
    Given a string s containing only digits, return the number of ways to decode it.
    The test cases are generated so that the answer fits in a 32-bit integer.
    
    Time Complexity: O(n)
    - Single pass through the string.
    
    Space Complexity: O(n)
    - DP map/array of size n is used. Could be optimized to O(1).
    """
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode string s[i:]
        dp = {len(s): 1}
        
        # Iterate backwards
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                # A "0" alone cannot be decoded
                dp[i] = 0
            else:
                # First, consider single digit decode
                dp[i] = dp[i + 1]
            
            # Second, check if two-digit decode is valid
            # Must be "10"-"19" or "20"-"26"
            if (i + 1 < len(s) and (s[i] == "1" or 
               (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]
                
        return dp[0]
