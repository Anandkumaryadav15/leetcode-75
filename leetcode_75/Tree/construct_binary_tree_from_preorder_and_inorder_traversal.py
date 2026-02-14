from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Construct Binary Tree from Preorder and Inorder Traversal
    
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    
    Time Complexity: O(n)
    - We process each node once. Finding index in 'inorder' takes time, but can be optimized with a hash map to O(1) lookup.
    
    Space Complexity: O(n)
    - Building the tree and recursion stack.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is always the root
        root = TreeNode(preorder[0])
        
        # Find the index of the root in inorder traversal to split left/right subtrees
        mid = inorder.index(preorder[0])
        
        # Left subtree elements in preorder: next 'mid' elements after root
        # Left subtree elements in inorder: all elements before 'mid'
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Right subtree elements in preorder: remaining elements
        # Right subtree elements in inorder: all elements after 'mid'
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root
