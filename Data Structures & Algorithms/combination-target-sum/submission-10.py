class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(index, cur, total):
            if index >= len(nums) or total > target:
                return
            if total == target:
                res.append(cur.copy())
                return
            
            cur.append(nums[index])
            dfs(index, cur, total + nums[index])
            cur.pop()
            dfs(index + 1, cur, total)
        dfs(0, [], 0)
        return res    
