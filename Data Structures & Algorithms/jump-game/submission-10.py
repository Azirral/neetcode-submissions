class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_reachable = set([len(nums) - 1])
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= (len(nums) - i -1):
                end_reachable.add(i)
            reachable = False
            for j in end_reachable:
                if nums[i] >= (j - i):
                    reachable = True
            if reachable:
                end_reachable.add(i)
        
        return 0 in end_reachable
