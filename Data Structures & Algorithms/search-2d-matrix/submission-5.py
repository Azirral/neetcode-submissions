class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        
        while top <= bottom:
            middle = (top + bottom) // 2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break
        
        if not(top <= bottom):
            return False

        row = (top + bottom) // 2

        l, r = 0, len(matrix[row]) - 1
        row = matrix[row]
        while l <= r:
            middle = (l + r) // 2
            if target < row[middle]:
                r = middle - 1
            elif target > row[middle]:
                l = middle + 1
            else:
                return True

        return False 
