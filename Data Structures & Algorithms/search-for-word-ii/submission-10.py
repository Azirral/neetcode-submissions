class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree():
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.word = True
    
    def search(self, word):
        cur = self. root

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]
        
        return cur.word
    
    def startsWith(self, prefix):
        cur = self.root

        for p in prefix:
            if p not in cur.children:
                return False
            cur = cur.children[p]

        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = PrefixTree()
        res = set()
        for word in words: 
            tree.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(cur, i, j, path):
            if cur.word:
                res.add(path)
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return

            for letter, child in cur.children.items():
                if board[i][j] == letter:
                    board[i][j] = "."
                    dfs(child, i - 1, j, path + letter)
                    dfs(child, i + 1, j, path + letter)
                    dfs(child, i, j - 1, path + letter)
                    dfs(child, i, j + 1, path + letter)
                    board[i][j] = letter

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(tree.root, i, j, "")

        return list(res)
