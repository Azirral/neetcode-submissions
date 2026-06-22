class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        for i in range(len(nums)):
            if nums[i] == 0:
                curr_min, curr_max = 1, 1
                continue
            tmp = curr_max * nums[i]
            curr_max = max(tmp, curr_min * nums[i], nums[i])
            curr_min = min(tmp, curr_min * nums[i], nums[i])
            res = max(res, curr_max)
        return res
        

