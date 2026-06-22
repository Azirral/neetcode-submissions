class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prev = 1
        for i in range(len(nums)):
            multiplication = 1
            for j in range(i + 1, len(nums)):
                multiplication *= nums[j]
            res.append(multiplication * prev)
            prev *= nums[i]
        
        return res
