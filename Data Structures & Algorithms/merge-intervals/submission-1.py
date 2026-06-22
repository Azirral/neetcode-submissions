class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        for i in range(1, len(intervals)):
            merging_interval = intervals[i - 1]
            if merging_interval[1] >= intervals[i][0]:
                merging_interval[0] = min(merging_interval[0], intervals[i][0])
                merging_interval[1] = max(merging_interval[1], intervals[i][1])
                intervals[i] = merging_interval
            else:
                res.append(merging_interval)
            
        res.append(intervals[-1])
        return res
            
                