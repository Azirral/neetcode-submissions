class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # start with a sliding window of length 2
        # count occurences by updating the dictionary
        # if the count 
        maxF = 0
        res = 0
        counts = {}
        l = 0
        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            if (counts[s[r]] > maxF):
                maxF += 1

            if ((r - l + 1) - maxF) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
