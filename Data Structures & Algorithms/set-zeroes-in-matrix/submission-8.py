class Capture:
    row_for_deletion = 'r'
    col_for_deletion = 'c'
    both = 'b'


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        def mark_row_for_deletion(r):
            nonlocal matrix
            val = matrix[r][0]

            match val:
                case Capture.col_for_deletion:
                    matrix[r][0] = Capture.both
                case Capture.both:
                    matrix[r][0] = Capture.both
                case _:
                    matrix[r][0] = Capture.row_for_deletion
            
        def mark_col_for_deletion(c):
            nonlocal matrix
            val = matrix[0][c]
            
            match val:
                case Capture.row_for_deletion:
                    matrix[0][c] = Capture.both
                case Capture.both:
                    matrix[0][c] = Capture.both
                case _:
                    matrix[0][c] = Capture.col_for_deletion

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    # mark row for deletion:
                    mark_col_for_deletion(c)
                    mark_row_for_deletion(r)


        for c in range(1, n):
            if matrix[0][c] == Capture.col_for_deletion or matrix[0][c] == Capture.both:
                for r in range(m):
                    matrix[r][c] = 0

        for r in range(1, m):
            if matrix[r][0] == Capture.row_for_deletion or matrix[r][0] == Capture.both:
                for c in range(n):
                    matrix[r][c] = 0

        if matrix[0][0] == Capture.row_for_deletion:
            for c in range(n):
                matrix[0][c] = 0


        if matrix[0][0] == Capture.col_for_deletion:
            for r in range(m):
                matrix[r][0] = 0

        if matrix[0][0] == Capture.both:
            for c in range(n):
                matrix[0][c] = 0 
            for r in range(m):
                matrix[r][0] = 0


        