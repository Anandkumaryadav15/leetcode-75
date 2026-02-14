from typing import List

class Solution:
    """
    Problem: Jump Game
    
    You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    
    Time Complexity: O(n)
    - Uses a greedy approach with a single pass backward.
    
    Space Complexity: O(1)
    - Only stores the goal linear index.
    """
    def canJump(self, nums: List[int]) -> bool:
        # The target destination is the last index
        goal = len(nums) - 1
        
        # Iterate backwards from second to last element
        for i in range(len(nums) - 1, -1, -1):
            # If from index i we can jump far enough to reach or pass the current goal,
            # then index i becomes the new goal.
            if i + nums[i] >= goal:
                goal = i
                
        # If the goal shifted all the way to 0, it means we can reach the end from the start
        return True if goal == 0 else False
