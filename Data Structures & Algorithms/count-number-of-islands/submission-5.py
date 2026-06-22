class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def bfs(r, c):
            q = collections.deque([[r, c]])
            visited.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc

                    if (r in range(ROWS) and
                        c in range(COLS) and
                        (r, c) not in visited and
                        grid[r][c] == "1"):
                        q.append([r, c])
                        visited.add((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands