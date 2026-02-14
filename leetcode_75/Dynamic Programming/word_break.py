from typing import List

class Solution:
    """
    Problem: Word Break
    
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
    
    Time Complexity: O(n * m * k)
    - n is length of string s.
    - m is number of words in wordDict.
    - k is the average length of words in wordDict (for string matching/slicing).
    
    Space Complexity: O(n)
    - DP array of size n + 1.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means s[i:] (suffix starting from i) can be broken into valid words
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True # Base case: empty string is valid
        
        # Iterate backwards from the end of the string
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if the word w matches pattern starting at s[i]
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # If match, then dp[i] status depends on the status of the rest of the string
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
                    
        return dp[0]
