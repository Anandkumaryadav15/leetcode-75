from typing import List

class Solution:
    """
    Problem: Container With Most Water
    
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    Return the maximum amount of water a container can store.
    
    Time Complexity: O(n)
    - We traverse the array with two pointers, meeting in the middle.
    
    Space Complexity: O(1)
    - Only a few variables used.
    """
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Area is limited by the shorter line
            # Width is the distance between indices
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to the shorter line inward
            # because to maximize area, we hope to find a taller line.
            # Moving the taller pointer wouldn't help because the height is limited by the shorter one.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
