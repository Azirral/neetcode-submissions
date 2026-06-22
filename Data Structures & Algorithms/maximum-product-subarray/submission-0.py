class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = float("-inf")

        for i in range(len(nums)):
            currProduct = 1
            for j in range(i, len(nums)):
                currProduct *= nums[j]
                maxProduct = max(maxProduct, currProduct)
        
        return maxProduct

        