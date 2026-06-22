class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Input: nums - array of n + 1 integers, integers are in the range of [1, n]
        # Constraints: array will always have at least two numbers
        #              individual numbers will be always from 1 up to n (including)
        #              n will be at least equal to 1
        # Output: duplicate integer
        # Intuition:
        #            if we have a list of two nodes, then the number that appears twice is either of the nodes
        #            hashset - would be easiest, so let's first do the approach with the hashset
        # Approach: 1. Initialize the seen hashset
        #           2. Iterate over elements of the array
        #           3. Checking if the number is already present in the hashset
        #           4. If it is then return the number
        #           5. Otherwise add the number to the hashset
        # Approach: 1. Sort the array ascendingly
        # Approach: 2. if nums[i] == nums[i + 1]
        #                return nums[i]
        # Approach: 1. Fast and slow pointers
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (nums[slow] == nums[fast]):
                break
        
        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow2