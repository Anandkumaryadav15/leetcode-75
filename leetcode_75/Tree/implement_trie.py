class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    """
    Problem: Implement Trie (Prefix Tree)
    
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
    Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
    
    Time Complexity: O(L) for each operation
    - Where L is the length of the word inserted/searched.
    
    Space Complexity: O(N * L)
    - Where N is the total number of words and L is the average length.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        # Traverse down the tree, creating nodes if they don't exist
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # Mark the end of the word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            # If char not found, word doesn't exist
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # Must end at a marked endOfWord node for full word match
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        # Prefix exists if we can traverse the whole prefix
        return True
