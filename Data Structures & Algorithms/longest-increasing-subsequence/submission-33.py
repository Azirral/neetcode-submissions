class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            localMax = 1
            for j in range(i + 1, len(nums), 1):
                if nums[j] > nums[i]:
                    temp = 1 + dp[j]
                    localMax = max(localMax, temp)
                    dp[i] = localMax

        return max(dp)
        
        
