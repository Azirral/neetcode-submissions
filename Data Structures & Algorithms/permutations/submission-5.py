class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                perm.append(nums[i])
                dfs(perm)
                seen.remove(nums[i])
                perm.pop()
            
        dfs([])
        return res