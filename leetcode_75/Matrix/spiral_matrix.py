from typing import List

class Solution:
    """
    Problem: Spiral Matrix
    
    Given an m x n matrix, return all elements of the matrix in spiral order.
    
    Time Complexity: O(m * n)
    - We visit each element once.
    
    Space Complexity: O(1)
    - Excluding the output array.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # 1. Get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # 2. Get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # Check if we are done (intervals might have crossed)
            if not (left < right and top < bottom):
                break
            
            # 3. Get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            
            # 4. Get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
        return res
