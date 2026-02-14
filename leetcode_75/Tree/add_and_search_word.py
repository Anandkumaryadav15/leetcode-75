class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    """
    Problem: Design Add and Search Words Data Structure
    
    Design a data structure that supports adding new words and finding if a string matches any previously added string.
    Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
    
    Time Complexity:
    - addWord: O(L), where L is the length of the word.
    - search: O(M), where M is the total number of characters in the Trie. Worst case we visit all nodes if word consists of all dots.
    
    Space Complexity: O(N * L)
    - Where N is number of words, L is average length.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        # Use simple DFS to handle the '.' wildcard
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                # If wildcard, check ALL children
                if c == ".":
                    for child in cur.children.values():
                        # If any path works, return True
                        if dfs(i + 1, child):
                            return True
                    return False
                    
                # Standard trie traversal
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                    
            return cur.word
            
        return dfs(0, self.root)
