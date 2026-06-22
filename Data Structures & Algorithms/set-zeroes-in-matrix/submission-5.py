class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zeros = set()
        cols_to_zeros = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows_to_zeros.add(r)
                    cols_to_zeros.add(c)

        for row in rows_to_zeros:
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
        
        for col in cols_to_zeros:
            for r in range(len(matrix)):
                matrix[r][col] = 0
        