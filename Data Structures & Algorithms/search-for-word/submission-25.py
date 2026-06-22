class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False
        def dfs(i, j, res, index):
            nonlocal exists
            if (index >= len(word) 
                or i < 0 or i >= len(board) 
                or j < 0 or j >= len(board[0])
                or board[i][j] != word[index]
                or board[i][j] == '!'):
                return

            char = board[i][j]
            res.append(char)
            
            if "".join(res) == word:
                exists = True
                return
                
            board[i][j] = '!'
            dfs(i, j + 1, res, index + 1)
            dfs(i, j - 1, res, index + 1)
            dfs(i + 1, j, res, index + 1)
            dfs(i - 1, j, res, index + 1)
            board[i][j] = char
            res.pop()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, [], 0)
        
        return exists