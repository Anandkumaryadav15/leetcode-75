from typing import List

class Solution:
    """
    Problem: Contains Duplicate
    
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
    Time Complexity: O(n)
    - We scan the array once.
    
    Space Complexity: O(n)
    - We use a set to store unique elements.
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a hash set to store elements we have seen
        seen = set()
        
        for num in nums:
            # If the number is already in the set, we found a duplicate
            if num in seen:
                return True
            # Add the number to the set
            seen.add(num)
            
        # No duplicates found
        return False
