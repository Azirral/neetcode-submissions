class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(curPath, target, curr):
            if curr >= len(nums) or target < 0:
                return
            if target == 0:
                res.append(curPath.copy())
                return
            
            curPath.append(nums[curr])
            dfs(curPath, target - nums[curr], curr)
            curPath.pop()
            dfs(curPath, target, curr + 1)
        
        dfs([], target, 0)
        return res
