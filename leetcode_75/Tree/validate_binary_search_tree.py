from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Validate Binary Search Tree
    
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    A valid BST is defined as follows:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.
    
    Time Complexity: O(n)
    - We traverse every node once.
    
    Space Complexity: O(h)
    - Recursion stack depth.
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Use helper function to pass valid range constraints down the tree
        def valid(node, left, right):
            if not node:
                return True
            
            # Current node value must be strictly between left and right bounds
            if not (left < node.val < right):
                return False
            
            # For left child: upper bound becomes current node value
            # For right child: lower bound becomes current node value
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
            
        # Initial call with infinity bounds
        return valid(root, float("-inf"), float("inf"))
