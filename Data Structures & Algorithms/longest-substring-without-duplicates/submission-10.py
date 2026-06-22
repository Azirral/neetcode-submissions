class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maxLength = 0
        curr = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[curr])
                curr += 1
            chars.add(s[i])
            maxLength = max(maxLength, i - curr + 1)    
        return maxLength