class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = {}
        counts_s2 = {}

        for i in range(len(s1)):
            counts_s1[s1[i]] = 1 + counts_s1.get(s1[i], 0)
        
        l, r = 0, 0
        while r < len(s2):
            if (counts_s1 == counts_s2):
                return True
            if (r - l) == len(s1):
                counts_s2[s2[l]] -= 1
                l += 1
            while ((r < len(s2) and not(s2[r] in counts_s1))):
                r += 1
                l = r
                counts_s2.clear()
            if (r == len(s2)):
                break
            counts_s2[s2[r]] = 1 + counts_s2.get(s2[r], 0)
            r += 1
        return counts_s1 == counts_s2
