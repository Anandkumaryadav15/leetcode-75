from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Maximum Depth of Binary Tree
    
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    
    Time Complexity: O(n)
    - We visit every node once.
    
    Space Complexity: O(h)
    - Where h is the height of the tree, corresponding to the recursion stack depth. In worst case (skewed tree), O(n).
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Depth is 1 (current node) + max depth of left or right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
