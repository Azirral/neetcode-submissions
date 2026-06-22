class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Maintain a stack of index, and height pairs
        # Pop from the stack, while the height isn't lower or equal than the new height
        # when popping, calculate the area of the rectangle by multiplying the difference between the new height's index and the index of the popping value
        # when newly inputted height, add it as the index of the last popped
        stack = []
        maxArea = 0
        for index, height in enumerate(heights):
            lastIndex = index
            while stack and stack[-1][1] > height:
                pop = stack.pop()
                lastIndex = pop[0]
                maxArea = max(maxArea, (index - lastIndex) * pop[1])
            stack.append((lastIndex, height))
        
        while stack:
            pop = stack.pop()
            maxArea = max(maxArea, (len(heights) - pop[0]) * pop[1])
        
        return maxArea
            
