from typing import List

class Solution:
    """
    Problem: Number of Connected Components in an Undirected Graph
    
    You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
    Return the number of connected components in the graph.
    
    Time Complexity: O(E * alpha(V)) ~= O(E)
    - Union-Find operations are nearly constant time on average.
    
    Space Complexity: O(V)
    - Parent and rank arrays.
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        # Find path compression
        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]] # Path compression
                res = parent[res]
            return res
            
        # Union by rank
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0 # Already connected
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
            
        res = n
        for n1, n2 in edges:
            # Every successful union decreases the number of connected components by 1
            res -= union(n1, n2)
            
        return res
