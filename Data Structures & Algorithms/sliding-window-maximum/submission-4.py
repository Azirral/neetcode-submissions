class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Intuition1: 1. Loop through array and insert each element into a Max Heap
        #             2. Once the window is of size k, take the root and insert it into the resulting list
        #             3. Remove the element at left pointer from the Heap, and add the element at right pointer + 1
        #             4. Take the root and insert into the resulting list
        #             5. Repeat steps 3 & 4 until the right pointer is equal to the last index of the array   

        # Intuition2: 1. Loop through array and insert each element into a list until the length of the list is equal to k
        #             2. Add the list to a list of lists
        #             3. Remove the first element from the list, and add the next element to the list
        #             4. Add the list to the list of lists
        #             5. Repeat 3&4 until the right pointer is equal to the last index of the array
        #             6. Loop through the list of lists, sorting each and extracting the max number to add to the result
        res = []
        l = r = 0
        dq = collections.deque()
        while r < len(nums):
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)
            if (l-1) == dq[0]:
                dq.popleft()
            if (r - l + 1) >= k:
                res.append(nums[dq[0]])
                l += 1

            r += 1
        
        return res