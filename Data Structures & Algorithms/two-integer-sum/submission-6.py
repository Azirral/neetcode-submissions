class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} 
        for i in range(len(nums)):
            check = target - nums[i]
            if check in hash_map:
                return [hash_map[check], i]
            hash_map[nums[i]] = i