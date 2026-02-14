from typing import List

class Solution:
    """
    Problem: 3Sum
    
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.
    
    Time Complexity: O(n^2)
    - Sorting takes O(n log n).
    - The nested loops take O(n^2).
    
    Space Complexity: O(1) or O(n) depending on implementation of sort
    - We ignore output array space. Sorting might take O(n) space.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer technique
        res = []
        
        for i in range(len(nums) - 2):
            # Skip positive integers since sum can't be 0
            if nums[i] > 0:
                break
            
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Two pointer approach for the remaining two elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Need a larger sum
                elif total > 0:
                    right -= 1 # Need a smaller sum
                else:
                    # Found a triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return res
