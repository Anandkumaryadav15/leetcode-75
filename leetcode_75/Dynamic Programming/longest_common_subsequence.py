class Solution:
    """
    Problem: Longest Common Subsequence
    
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
    
    Time Complexity: O(m * n)
    - Where m and n are lengths of the two strings. We fill a 2D grid.
    
    Space Complexity: O(m * n)
    - To store the 2D DP grid.
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create a 2D grid initialized with 0s. 
        # Dimensions are (len(text1) + 1) x (len(text2) + 1) to handle base cases (empty strings).
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        
        # Iterate backwards
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If characters match, add 1 to the result of the remaining strings (diagonal)
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # If they don't match, take the max of skipping a char from text1 OR skipping a char from text2
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                    
        return dp[0][0]
