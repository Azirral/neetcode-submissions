class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        res = 0
        i = 1
        n = len(intervals)
        while (i < n):
            if intervals [i][0] >= intervals[i-1][0] and intervals[i][0] < intervals[i - 1][1]:
                res += 1
                n -= 1
                if intervals[i][1] > intervals[i - 1][1]:
                    intervals.pop(i)
                    continue
                else:
                    intervals.pop(i - 1)
                    continue
            else:
                i += 1
        return res
