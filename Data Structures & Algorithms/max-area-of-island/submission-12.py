class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1. Input: grid - 2 dimensional list of lists, where each cell can be either a 1 or a 0
        #           if it is a 1 - then that cell is interpreted as land
        #           if it is a 0 - then that cell is interpreted as water
        #           the cells beyond the grid are assumed to be water
        # Definition:
        #            An island is a group of 1's either connected vertically or horizontally
        # !!!!!!!!!! - the ones that are on the diagonals are not considered to be part of the same group of 1's
        #              and consequently island's
        # 2. Output: maxArea - the biggest area of an island within the board
        # 3. Approach: Run a dfs algorithm, which will mark the islands as visited, and count the cells of the same island.
        # 4. Then, the area will be compared with the maxArea and maxArea will be updated accordingly

        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0

            area = (1 + dfs(r - 1, c) + 
                        dfs(r + 1, c) + 
                        dfs(r, c - 1) + 
                        dfs(r, c + 1)) 

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea