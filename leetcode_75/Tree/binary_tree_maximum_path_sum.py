from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Binary Tree Maximum Path Sum
    
    A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
    The path sum is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    
    Time Complexity: O(n)
    - We visit every node once.
    
    Space Complexity: O(h)
    - Recursion stack.
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val] # Global maximum sum found so far
        
        # Steps:
        # 1. Compute max path sum for left child and right child.
        # 2. Max path sum passing THROUGH current node (splitting path) = node.val + maxLeft + maxRight.
        # 3. Update global max with (2).
        # 4. Return max path sum extendable to parent = node.val + max(maxLeft, maxRight).
        
        def dfs(root):
            if not root:
                return 0
            
            # Recursively get max path sum from children. 
            # If negative, we ignore that branch (max(0, ...)).
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # Compute max path sum WITH split at current node
            # This path includes left child path + current node + right child path
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # Return max path sum without split (only one branch can be chosen)
            return root.val + max(leftMax, rightMax)
            
        dfs(root)
        return res[0]
