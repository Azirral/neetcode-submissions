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
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)
