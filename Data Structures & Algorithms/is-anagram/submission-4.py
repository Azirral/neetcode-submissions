class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occurences_s = {}
        occurences_t = {}
        for i, j in zip(s, t):
            value_s = 1 if not(i in occurences_s) else (occurences_s[i] + 1)
            value_t = 1 if not(j in occurences_t) else (occurences_t[j] + 1)
            occurences_s.update({i : value_s})
            occurences_t.update({j : value_t})
        return occurences_s == occurences_t
