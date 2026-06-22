class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        first_prev = 2
        second_prev = 1
        def dfs():
            nonlocal first_prev, second_prev
            res = first_prev + second_prev
            second_prev = first_prev
            first_prev = res
            return res
        res = 0
        for i in range(n - 2):
            res = dfs()
        return res