from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word):
        cur = self
        
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= ROWS or c >=COLS 
                or board[r][c] not in node.children 
                or (r,c) in visited):
                return 
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)
                
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            
            visited.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
                
        return list(res)
        
        
        
        