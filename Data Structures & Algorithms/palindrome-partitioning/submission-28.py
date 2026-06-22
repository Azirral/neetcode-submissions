class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def backtrack(index):
            if index >= len(s):
                res.append(part.copy())
                return

            for i in range(index, len(s)):
                cur = s[index:i + 1]
                copy = cur
                if copy[::-1] == cur:
                    part.append(cur)
                    backtrack(i + 1)
                    part.pop()
            
        backtrack(0)
        return res