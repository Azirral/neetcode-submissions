class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = False
        counts_s1, counts_s2 = [0] * 26, [0] * 26
        if (len(s1) > len(s2)):
            return res
        for i in range(len(s1)):
            counts_s1[ord(s1[i]) - ord('a')] += 1
            counts_s2[ord(s2[i]) - ord('a')] += 1
        matching = 0
        for i in range(26):
            matching += (1 if counts_s1[i] == counts_s2[i] else 0)
        l = 0
        
        for r in range(len(s1), len(s2)):
            if matching == 26:
                res = True

            i = ord(s2[r]) - ord('a')
            counts_s2[i] += 1
            if counts_s1[i] == counts_s2[i]:
                matching += 1
            elif counts_s1[i] + 1 == counts_s2[i]:
                matching -= 1
            
            i = ord(s2[l]) - ord('a')
            counts_s2[i] -= 1

            if counts_s1[i] == counts_s2[i]:
                matching += 1
            elif counts_s1[i] - 1 == counts_s2[i]:
                matching -= 1
            l += 1
        if matching == 26:
                res = True
        return res    
