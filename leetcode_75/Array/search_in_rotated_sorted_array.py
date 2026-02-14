from typing import List

class Solution:
    """
    Problem: Search in Rotated Sorted Array
    
    There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index.
    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.
    
    Time Complexity: O(log n)
    - Binary search is used.
    
    Space Complexity: O(1)
    - Constant extra space.
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            # If nums[left] <= nums[mid], it means the pivot is in the right half or at mid,
            # so the left side is strictly increasing.
            if nums[left] <= nums[mid]:
                # If target is within the sorted left half range, look there
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise, target must be in the right half
                else:
                    left = mid + 1
            # If left half is not sorted, the right half MUST be sorted
            else:
                # If target is within the sorted right half range, look there
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise, target must be in the left half
                else:
                    right = mid - 1
                    
        return -1
