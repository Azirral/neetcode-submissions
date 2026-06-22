class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums_without_first = nums[1:]
        nums_without_last = nums[:-1]
        
        def maxRob(numbers):
            rob1, rob2 = 0, 0
            for n in numbers:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(maxRob(nums_without_first), maxRob(nums_without_last))
        