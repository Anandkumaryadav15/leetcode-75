from typing import List

class Solution:
    """
    Problem: Two Sum
    
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    
    Time Complexity: O(n)
    - We traverse the list containing n elements exactly once.
    - Each lookup in the table costs only O(1) time.
    
    Space Complexity: O(n)
    - The extra space required depends on the number of items stored in the hash table, which stores at most n elements.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store number: index
        num_map = {}
        
        for i, num in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - num
            
            # Check if the difference is already in the map
            # If it is, we found our pair
            if diff in num_map:
                return [num_map[diff], i]
            
            # Otherwise, store the current number and its index
            num_map[num] = i
            
        return []
