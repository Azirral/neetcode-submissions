class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        uniq_paths = [[0] * (n+1)] * (m + 1)
        uniq_paths[m-1][n-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                uniq_paths[i][j] = uniq_paths[i+1][j] + uniq_paths[i][j+1]
        
        return uniq_paths[0][0]

