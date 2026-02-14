class Solution:
    """
    Problem: Longest Palindromic Substring
    
    Given a string s, return the longest palindromic substring in s.
    
    Time Complexity: O(n^2)
    - We expand around the center for each character (2n - 1 centers). Each expansion takes O(n).
    
    Space Complexity: O(1)
    - We only store the indices of the best palindrome found.
    """
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # Odd length palindromes (single character center)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # Even length palindromes (two character center)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res
