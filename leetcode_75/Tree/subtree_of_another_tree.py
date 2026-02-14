from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Subtree of Another Tree
    
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    
    Time Complexity: O(m * n)
    - Where m is nodes in root, n is nodes in subRoot. In worse case we check SameTree for every node in root.
    
    Space Complexity: O(min(m, n))
    - Recursion stack depth.
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        # If structure and values match exactly starting from current root
        if self.sameTree(root, subRoot):
            return True
        
        # Otherwise, check left or right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
    
    # Helper function to check if two trees are identical
    def sameTree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self.sameTree(r.left, s.left) and
                    self.sameTree(r.right, s.right))
        return False
