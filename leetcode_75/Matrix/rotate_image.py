from typing import List

class Solution:
    """
    Problem: Rotate Image
    
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    
    Time Complexity: O(n^2)
    - We touch every element.
    
    Space Complexity: O(1)
    - In-place rotation.
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            # Iterate through the range of the current layer
            for i in range(r - l):
                top, bottom = l, r
                
                # Save the topleft value
                topLeft = matrix[top][l + i]
                
                # Move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # Move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # Move top left into top right
                matrix[top + i][r] = topLeft
                
            # Move to the inner layer
            r -= 1
            l += 1
