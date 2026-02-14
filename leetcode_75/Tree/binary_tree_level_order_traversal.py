from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Problem: Binary Tree Level Order Traversal
    
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
    
    Time Complexity: O(n)
    - We visit every node once using BFS.
    
    Space Complexity: O(n)
    - Queue can hold up to n/2 nodes (widest level).
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        
        # Standard BFS loop
        while q and root:
            val = []
            lenQ = len(q)
            # Process entire level at once
            for i in range(lenQ):
                node = q.pop(0)
                val.append(node.val)
                # Add children to queue for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res
