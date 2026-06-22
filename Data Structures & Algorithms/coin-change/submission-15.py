class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_unique = set(coins)
        coins_sorted = list(coins_unique)
        dp = {} # this will store our intermediary results to reduce the number of computations needed.

        def dfs(target):
            nonlocal coins_sorted
            if target == 0:
                return 0

            res = float("inf") # If there's no solution 

            for coin in coins_sorted:
                # if target in dp res = min (res, target)
                # if target in dp but target = float("inf") then no solution is found
                # if target - coin >= 0 we return 
                if target in dp:
                    res = min(res, dp[target])
                    continue
                if (target - coin) >= 0:
                    res = min(res, 1 + dfs(target - coin))
            dp[target] = res
            return res
        
        res = dfs(amount)

        if res == float("inf"):
            return -1
        return res
        