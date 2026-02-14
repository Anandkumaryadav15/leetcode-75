from typing import List

class Solution:
    """
    Problem: Course Schedule
    
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
    Return true if you can finish all courses. Otherwise, return false.
    Essentially, detect if there is a cycle in the directed graph.
    
    Time Complexity: O(V + E)
    - Standard DFS cycle detection
    
    Space Complexity: O(V + E)
    - Adjacency list and recursion stack.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites list
        preMap = { i:[] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # Set to keep track of courses currently being visited in the current DFS path
        visitSet = set()
        
        def dfs(crs):
            # If course is already in visitSet, we found a cycle
            if crs in visitSet:
                return False
            # If course has no prerequisites, it can be completed
            if preMap[crs] == []:
                return True
                
            visitSet.add(crs)
            # Check all prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # Remove from visitSet after visiting all neighbors (backtracking)
            visitSet.remove(crs)
            
            # Optimization: Mark as having no prerequisites so we don't re-check valid subgraphs
            preMap[crs] = []
            return True
            
        # Check every course (graph might not be fully connected)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
