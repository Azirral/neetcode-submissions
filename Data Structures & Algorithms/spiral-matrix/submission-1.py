class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction_change = {"right":"down", "down":"left", "left": "up", "up":"right"}
        res = []
        m = len(matrix)
        n = len(matrix[0])
        direction = "right"
        def is_border(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] is None):
                return True
            return False
        
        def next_position(direction, i, j):
            match direction:
                case "right":
                    return (i, j + 1)
                case "down":
                    return (i + 1, j)
                case "left":
                    return (i, j - 1)
                case "up":
                    return (i - 1, j)
        
        spiral_continueing = True
        r, c = 0, 0
        while spiral_continueing:
            res.append(matrix[r][c])
            temp_r, temp_c = next_position(direction, r, c)
            if is_border(temp_r, temp_c):
                direction = direction_change[direction]
                temp_r, temp_c = next_position(direction, r, c)
                if is_border(temp_r, temp_c):
                    spiral_continueing = False
            matrix[r][c] = None
            r, c = temp_r, temp_c 
        return res
        