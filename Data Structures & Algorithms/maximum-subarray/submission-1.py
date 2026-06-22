class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sums = [num for num in nums]
        res = nums[0]
        for i in range(1, len(nums)):
            temp_sum = curr_sums[i - 1] + nums[i]
            if temp_sum > curr_sums[i]:
                curr_sums[i] = temp_sum
            res = max(res, curr_sums[i])
        return res