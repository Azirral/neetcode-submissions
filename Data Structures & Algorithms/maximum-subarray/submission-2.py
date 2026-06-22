class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sums = [num for num in nums]
        res = nums[0]
        for i in range(1, len(nums)):
            curr_sums[i] = max(curr_sums[i], curr_sums[i] + curr_sums[i - 1])
            res = max(res, curr_sums[i])
        return res