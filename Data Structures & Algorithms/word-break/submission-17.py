class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {i:False for i in range(len(s))} # For storing false paths
        i = len(s) - 1
        while i >= 0: 
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    if i + len(word) == len(s) or dp[i + len(word)] == True: 
                        dp[i] = True
            i -= 1
        
        return dp[0]
