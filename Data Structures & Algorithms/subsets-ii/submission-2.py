class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, cur):
            if index >= len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[index])
            dfs(index + 1, cur)
            pop = cur.pop()
            
            while index < len(nums) and pop == nums[index]:
                index += 1
            dfs(index, cur)
        
        dfs(0, [])
        return res
