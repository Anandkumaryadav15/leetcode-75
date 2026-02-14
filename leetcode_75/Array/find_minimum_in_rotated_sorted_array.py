from typing import List

class Solution:
    """
    Problem: Find Minimum in Rotated Sorted Array
    
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.
    You must write an algorithm that runs in O(log n) time.
    
    Time Complexity: O(log n)
    - Binary search is used.
    
    Space Complexity: O(1)
    - Iterative binary search uses constant space.
    """
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum element must be in the right half (excluding mid).
            # e.g., [3, 4, 5, 1, 2] -> mid=5 > right=2 -> go right
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than or equal to the rightmost element,
            # the minimum is in the left half (including mid).
            # e.g., [5, 1, 2, 3, 4] -> mid=2 < right=4 -> go left
            else:
                right = mid
                
        # When left == right, we have found the minimum element
        return nums[left]
