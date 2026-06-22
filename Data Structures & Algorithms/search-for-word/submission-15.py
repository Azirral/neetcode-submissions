class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        self.res = False
        def backtrack(r, c, cur, index):
            if cur == word:
                self.res = True
                return 
            if (r >= ROWS or c >= COLUMNS or 
            r < 0 or c < 0 or index >= len(word) or 
            board[r][c] != word[index] or board[r][c] == "!"):
                return 

            cur += board[r][c]
            temp = board[r][c]
            board[r][c] = "!"
            backtrack(r + 1, c, cur, index + 1) 
            backtrack(r - 1, c, cur, index + 1) 
            backtrack(r, c + 1, cur, index + 1) 
            backtrack(r, c - 1, cur, index + 1)
            board[r][c] = temp
            return 

        for i in range(ROWS):
            for j in range(COLUMNS):
                if board[i][j] == word[0]:
                    backtrack(i, j, "", 0)
        
        return self.res