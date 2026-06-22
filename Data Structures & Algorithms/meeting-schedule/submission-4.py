"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if len(intervals) <= 1: return True
        prevEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start >= prevEnd:
                prevEnd = interval.end
            else:
                return False
        return True