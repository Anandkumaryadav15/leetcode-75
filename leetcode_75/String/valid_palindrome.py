class Solution:
    """
    Problem: Valid Palindrome
    
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
    Given a string s, return true if it is a palindrome, or false otherwise.
    
    Time Complexity: O(n)
    - We iterate through the string using two pointers.
    
    Space Complexity: O(1)
    - We do it in-place without creating a new filtered string.
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer until alphanumeric char found
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move right pointer until alphanumeric char found
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        # Helper to check if char is alphanumeric
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
