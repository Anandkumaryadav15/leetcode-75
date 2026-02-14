from typing import List

class Solution:
    """
    Problem: Encode and Decode Strings
    
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
    
    Time Complexity: O(n)
    - We iterate through all characters of all strings.
    
    Space Complexity: O(1)
    - Excluding the output string/list.
    """
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs: List[str]) -> str:
        res = ""
        # Format: length + # + string
        # e.g., ["abc", "de"] -> "3#abc2#de"
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str: str) -> List[str]:
        res, i = [], 0
        
        while i < len(str):
            j = i
            # Find the next delimiter
            while str[j] != "#":
                j += 1
            # Parse the length
            length = int(str[i : j])
            # Extract the string using the length
            res.append(str[j + 1 : j + 1 + length])
            # Move index to the start of the next encoded string
            i = j + 1 + length
        return res
