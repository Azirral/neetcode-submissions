class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        maxLength = 0
        curr = 0
        for i in range(len(s)):
            if s[i] in chars:
                curr = max(chars[s[i]] + 1, curr)
            chars[s[i]] = i
            maxLength = max(maxLength, i - curr + 1)
        return maxLength