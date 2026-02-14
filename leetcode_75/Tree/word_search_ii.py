from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    """
    Problem: Word Search II
    
    Given an m x n board of characters and a list of strings words, return all words on the board.
    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
    
    Time Complexity: O(m * n * 4^L)
    - where m*n is board size, L is max length of word. With Trie pruning, it's much faster than simple DFS for each word.
    
    Space Complexity: O(K * L)
    - To store K words of length L in Trie.
    """
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a Trie from the words list for efficient prefix lookup
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            # Found a char in Trie, move deeper
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            
            # If we found a full word, add to result set
            if node.isWord:
                res.add(word)
                # Optimization: Could mark node.isWord = False to avoid duplicates
                # Or remove the word from Trie to prune search space further
                
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c)) # Backtrack
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
                
        return list(res)
