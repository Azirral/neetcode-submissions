class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Input: stones - weights of stones
        # Output: last remaining stone's weight
        # Intuition: maxHeap 
        # Approach: 1. Heapify the weights
        #           2. Initialize the res = 0 -- Unnecessary
        #           3. perform a loop while the length of the heap is bigger than 1
        #           4. Each iteration pop two elements from the heap
        #           5. If they are of equal weight, continue the loop
        #           6. If one stone is of lower weight,
        #              then the stone with bigger weight is adjusted
        #              by subtracting the lower value from it and pushing it back onto the heap
        #           7. Once the loop ends, if there's no elements in the heap return 0
        #           8. Otherwise return the last element

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            x = (-1) * heapq.heappop(stones)
            y = (-1) * heapq.heappop(stones)

            if x == y:
                continue
            item = (-1) * (max(x, y) - min(x, y))
            heapq.heappush(stones, item)
        
        if len(stones) == 1:
            return ((-1) * heapq.heappop(stones))
        
        return 0
        
