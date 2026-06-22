class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        if len(position) == 1:
            return 1
        
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort()

        for i in range(len(cars)):
            cars[i] = float(target - cars[i][0]) / cars[i][1]
        
        stack = []
        stack.append(cars[-1])
        for i in range(len(cars) - 1, -1, -1):
            if cars[i-1] > stack[-1]:
                stack.append(cars[i-1])
        
        return len(stack)
