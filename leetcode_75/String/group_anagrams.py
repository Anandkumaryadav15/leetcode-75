from typing import List
from collections import defaultdict

class Solution:
    """
    Problem: Group Anagrams
    
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    
    Time Complexity: O(m * n)
    - where m is the number of strings and n is the average length of a string. 
    - We iterate through each string and count its characters (O(n)).
    
    Space Complexity: O(m * n)
    - To store the result.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams
        
        for s in strs:
            # We use an array of size 26 as the key for the hash map
            # This is better than sorting the string which would take O(n log n)
            count = [0] * 26 # a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # Lists are mutable and cannot be keys, so we convert to tuple
            res[tuple(count)].append(s)
            
        return list(res.values())
