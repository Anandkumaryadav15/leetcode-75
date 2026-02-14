from typing import List

class Solution:
    """
    Problem: Set Matrix Zeroes
    
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.
    
    Time Complexity: O(m * n)
    - We iterate through the matrix twice.
    
    Space Complexity: O(1)
    - We use the first row and first column as markers to avoid O(m+n) extra space.
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False # Flag for the first row specifically
        
        # 1. Determine which rows/cols need to be zero by marking first row/col
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0 # Mark column
                    if r > 0:
                        matrix[r][0] = 0 # Mark row
                    else:
                        rowZero = True
                        
        # 2. Zero out cells based on markers (skipping first row/col for now)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # 3. Handle the first column separately
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # 4. Handle the first row separately
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
