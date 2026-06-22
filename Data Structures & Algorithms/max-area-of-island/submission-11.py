class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            q = collections.deque([(r, c)])
            cur = 0
            grid[r][c] = 0
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            while q:
                row, col = q.popleft()
                cur += 1
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue

                    if grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        
            return cur 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
                
        return maxArea