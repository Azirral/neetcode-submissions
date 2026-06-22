class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        candidates = set(nums) 

        def dfs(perm, candidates):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for candidate in candidates:
                perm.append(candidate)
                copy = candidates.copy()
                copy.remove(candidate)
                dfs(perm, copy)
                perm.pop()
            
        dfs([], candidates)
        return res