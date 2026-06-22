class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visited or
                board[r][c] == 'X'):
                return
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        
        for r in range(ROWS):
            if ((r, 0) not in visited and board[r][0] == "O"):
                dfs(r, 0)
            if ((r, COLS - 1) not in visited and board[r][COLS - 1] == "O"):
                dfs(r, COLS - 1)
        
        for c in range(COLS):
            if ((0, c) not in visited and board[0][c] == "O"):
                dfs(0, c)
            if ((ROWS - 1, c) not in visited and board[ROWS - 1][c] == "O"):
                dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"

            