class Solution:
    """
    Problem: Unique Paths
    
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
    
    Time Complexity: O(m * n)
    - We fill out the grid cells.
    
    Space Complexity: O(n)
    - We only store the current row (optimized from O(m*n)).
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom row has only 1 way to reach end (only go right)
        row = [1] * n
        
        # Iterate from the second to last row up to the top
        for i in range(m - 1):
            newRow = [1] * n
            # Iterate backwards through columns
            # The rightmost column is always 1 (only go down)
            for j in range(n - 2, -1, -1):
                # Ways(r, c) = Ways(r+1, c) [down] + Ways(r, c+1) [right]
                # newRow[j+1] is right neighbor, row[j] is the neighbor below (from previous iteration)
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
            
        return row[0]
