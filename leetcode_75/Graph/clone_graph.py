from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    """
    Problem: Clone Graph
    
    Given a reference of a node in a connected undirected graph.
    Return a deep copy (clone) of the graph.
    Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
    
    Time Complexity: O(V + E)
    - We visit every vertex and edge once.
    
    Space Complexity: O(V)
    - Hash map stores each node visited.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Map old nodes to new nodes to handle cycles and avoid infinite recursion
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            # Create a copy
            copy = Node(node.val)
            oldToNew[node] = copy
            
            # Recursively copy neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
            
        return dfs(node) if node else None
