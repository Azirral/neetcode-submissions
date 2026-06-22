class Solution:
    def trap(self, height: List[int]) -> int:
        area  = 0
        l, r = 0, len(height) - 1
        prefix = [0] * len(height)
        postfix = [0] * len(height)
        highest_left = height[l]
        highest_right = height[r]
        while l < len(height) - 1 and r > 0:
            prefix[l] = highest_left
            postfix[r] = highest_right
            highest_left = max(height[l], highest_left)
            highest_right = max(height[r], highest_right)
            l += 1
            r -= 1
        for i in range(len(height)):
            area += max(min(postfix[i], prefix[i]) - height[i], 0)
        return area
             