class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        
        cur.endOfWord = True

    

    def search(self, word: str) -> bool:
        cur = self.root
        def dfs(cur, j):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False 
                if word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            
            return cur.endOfWord
        
        return dfs(cur, 0)
