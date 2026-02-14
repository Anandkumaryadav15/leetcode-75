class Solution:
    """
    Problem: Palindromic Substrings
    
    Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.
    
    Time Complexity: O(n^2)
    - We expand around center for all possible centers.
    
    Space Complexity: O(1)
    - Constant extra space.
    """
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # Odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # Even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
