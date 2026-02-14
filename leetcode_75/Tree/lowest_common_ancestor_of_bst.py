# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Problem: Lowest Common Ancestor of a Binary Search Tree
    
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
    
    Time Complexity: O(h)
    - Where h is the height of the tree because we only visit one node per level. O(log n) for balanced BST, O(n) for skewed.
    
    Space Complexity: O(1)
    - Iterative solution uses constant extra space.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start from the root
        cur = root
        
        while cur:
            # If both p and q are greater than current node, 
            # then LCA must be in the right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both p and q are smaller than current node,
            # then LCA must be in the left subtree.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # If we reach a split point where one is smaller and one is larger (or equal),
            # then current node is the LCA.
            else:
                return cur
