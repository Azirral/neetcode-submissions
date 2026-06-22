class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            minHeap.append([(point[0] ** 2 + point[1] ** 2), point[0], point[1]])

        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            pop = heapq.heappop(minHeap)
            res.append([pop[1], pop[2]])
        return res