from typing import List

class Solution:
    """
    Problem: Graph Valid Tree
    
    You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
    Return true if the edges of the given graph make up a valid tree, and false otherwise.
    A valid tree must be fully connected and contain no cycles.
    
    Time Complexity: O(V + E)
    - Depth First Search touches all nodes and edges.
    
    Space Complexity: O(V + E)
    - Adjacency list and recursion stack.
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        # Build adjacency list
        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            
        visit = set()
        
        def dfs(i, prev):
            # If node is already visited, we found a cycle
            if i in visit:
                return False
                
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue # Do not go back to the parent node we just came from
                if not dfs(j, i):
                    return False
            return True
            
        # 1. Check for cycles starting from node 0
        # 2. Check if the graph is connected (all nodes visited)
        return dfs(0, -1) and n == len(visit)
