class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeOfConsumption(k):
            res = 0
            for num in piles:
                if num % k == 0:
                    res += num / k
                else:
                    res += num // k + 1
            return res

        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            m = (l + r) // 2
            total = timeOfConsumption(m)
            if total <= h:
                res = m
                r = m - 1
            else: 
                l = m + 1
        
        return res


            

