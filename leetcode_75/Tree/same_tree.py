from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Same Tree
    
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
    
    Time Complexity: O(n)
    - We visit every node in both trees once.
    
    Space Complexity: O(h)
    - Recursion stack depth.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are None, they are identical (empty)
        if not p and not q:
            return True
        # If one is None but not the other, or values differ, they are not same
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
