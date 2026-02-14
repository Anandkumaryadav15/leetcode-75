from typing import List

class Solution:
    """
    Problem: Product of Array Except Self
    
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    
    Time Complexity: O(n)
    - We do two passes over the array.
    
    Space Complexity: O(1)
    - The output array does not count as extra space for the purpose of space complexity analysis.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        # Pass 1: Calculate prefix products
        # output[i] will contain the product of all elements to the left of i
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        
        # Pass 2: Calculate suffix products and combine
        # right keeps track of the product of all elements to the right
        right = 1
        for i in range(n - 1, -1, -1):
            # Multiply the current output[i] (which is prefix product) by the suffix product (right)
            output[i] *= right
            # Update right to include nums[i] for the next iteration
            right *= nums[i]
            
        return output
