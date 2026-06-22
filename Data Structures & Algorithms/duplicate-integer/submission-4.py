class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums[i+1:])):
                if (nums[i] == nums[j+i+1]):
                    return True
    
        return False