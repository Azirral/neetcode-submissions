class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)+1):
            count += i

        count2 = 0
        for num in nums:
            count2 += num
        return count - count2