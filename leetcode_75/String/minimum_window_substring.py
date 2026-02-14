class Solution:
    """
    Problem: Minimum Window Substring
    
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
    
    Time Complexity: O(m + n)
    - We iterate through s and t once.
    
    Space Complexity: O(m + n)
    - To store the frequency maps.
    """
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            # Check if the current character satisfies the requirement for that character in t
            if c in countT and window[c] == countT[c]:
                have += 1
                
            # While we have a valid window (all characters from t are present)
            while have == need:
                # Update our result if this window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                    
                # Shrink the window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""
