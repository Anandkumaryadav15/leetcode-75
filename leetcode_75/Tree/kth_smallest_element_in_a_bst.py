from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Kth Smallest Element in a BST
    
    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
    
    Time Complexity: O(H + k)
    - H is tree height. We go down to leftmost node (min value), then iterate k times.
    
    Space Complexity: O(H) or O(log n)
    - Stack stores nodes along path to root.
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root
        
        # Iterative Inorder Traversal (Left -> Root -> Right)
        # Inorder traversal of BST gives elements in sorted order
        while cur or stack:
            # Go as left as possible
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # Pop the smallest element available
            cur = stack.pop()
            n += 1
            
            # If it's the kth element, return it
            if n == k:
                return cur.val
                
            # Move right
            cur = cur.right
