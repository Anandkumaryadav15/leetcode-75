from typing import List

class Solution:
    """
    Problem: Alien Dictionary
    
    There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
    You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
    Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.
    
    Time Complexity: O(C)
    - Where C is the total length of all words in the input. We iterate through all characters.
    
    Space Complexity: O(1) or O(U + min(U^2, N))
    - Where U is unique characters (max 26) and N is number of words. Since U is small (26), space is constant.
    """
    def alienOrder(self, words: List[str]) -> str:
        # Initialize adjacency list for all unique characters
        adj = { c:set() for w in words for c in w }
        
        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # Edge case: "abc" before "ab" is invalid if "ab" is a prefix of "abc"
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Find the first differing character to determine order
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        # DFS for topological sort and cycle detection
        visit = {} # False=visited, True=visited & in current path
        res = []
        
        def dfs(c):
            if c in visit:
                # If True, we found a cycle (back edge to current path)
                # If False, we already processed this node, no need to re-process
                return visit[c]
                
            visit[c] = True # Mark as in current path
            
            for nei in adj[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False # Mark as visited but not in current path
            res.append(c)
            
        # Run DFS on all nodes
        for c in adj:
            if dfs(c):
                return ""
                
        # The result is built in reverse topological order
        res.reverse()
        return "".join(res)
