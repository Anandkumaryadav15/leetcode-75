from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Problem: Serialize and Deserialize Binary Tree
    
    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
    
    Time Complexity: O(n)
    - We visit every node once during serialization and once during deserialization.
    
    Space Complexity: O(n)
    - String and recursion stack.
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        # Preorder traversal (Root -> Left -> Right)
        def dfs(node):
            if not node:
                res.append("N") # Use 'N' for null
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        # Join with comma to separate values
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0 # Global pointer for recursion
        
        def dfs():
            # If current value is 'N', it's a null node
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            # Create node
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            
            # Recursively build left and right subtrees
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()
