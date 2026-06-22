class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Input: grid - 2d matrix filled with cells of three possible values
        #       0 - empty cell
        #       1 - fresh fruit
        #       2 - rotten fruit
        # Output: number of iterations for each fruit to be rotten
        #         -1 if such a state isn't possible
        # Intuition: a breadth-first-search algorithm running if new fruit can be rotten
        #          : Requires a final check if there are any fresh fruit left.

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        self.fresh = 0 
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        def addFruit(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] == 2 or
                grid[r][c] == 0):
                return
            
            visited.add((r, c))
            grid[r][c] = 2
            self.fresh -= 1
            q.append((r, c))

        
        while self.fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                visited.add((r, c))

                addFruit(r + 1, c)
                addFruit(r - 1, c)
                addFruit(r, c + 1)
                addFruit(r, c - 1)
            minutes += 1
        
        return minutes if self.fresh == 0 else -1