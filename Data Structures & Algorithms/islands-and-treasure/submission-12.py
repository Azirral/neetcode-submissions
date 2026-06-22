class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        water, treasure, land = -1, 0, 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == treasure:
                    q.append((r, c))
                    visited.add((r, c))

        def addRoom(r, c):
            if (r < 0 or
                r >= rows or
                c < 0 or 
                c >= cols or
                grid[r][c] == water or
                (r, c) in visited):
                return
            visited.add((r, c))
            q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    qr, qc = r + dr, c + dc
                    addRoom(qr, qc)
            dist += 1
         
