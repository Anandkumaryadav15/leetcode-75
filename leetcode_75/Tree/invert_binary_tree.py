from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Invert/Flip Binary Tree
    
    Given the root of a binary tree, invert the tree, and return its root.
    
    Time Complexity: O(n)
    - We visit every node once to swap its children.
    
    Space Complexity: O(h)
    - Recursion stack depth.
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap the left and right children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
