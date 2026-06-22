class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LCS = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for r in range(len(text1) - 1, -1, -1):
            for c in range(len(text2) - 1, -1, -1):
                if (text1[r] == text2[c]):
                    LCS[r][c] = 1 + LCS[r + 1][c + 1]
                else:
                    LCS[r][c] = max(LCS[r + 1][c], LCS[r][c + 1])
        return LCS[0][0]