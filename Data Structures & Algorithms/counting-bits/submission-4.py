class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        dp = {}
        dp[0] = 0
        offset = 1
        for i in range(1, n + 1):
            if i == (offset * 2):
                offset = i
            dp[i] = 1 + dp[i - offset]
            res.append(dp[i])
        
        return res