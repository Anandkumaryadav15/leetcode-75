class Solution:
    """
    Problem: Longest Substring Without Repeating Characters
    
    Given a string s, find the length of the longest substring without repeating characters.
    
    Time Complexity: O(n)
    - We use a sliding window approach with two pointers (l and r). Each character is visited at most twice.
    
    Space Complexity: O(min(m, n))
    - We need O(k) space for the set, where k is the size of the set. The size of the set is upper bounded by the size of the string n and the size of the charset m.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            # If we encounter a duplicate, shrink the window from the left until the duplicate is removed
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Add the current character to the set
            charSet.add(s[r])
            # Update the maximum length found so far
            res = max(res, r - l + 1)
        return res
