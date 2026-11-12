"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i:i.start)
        time = [intervals[0].end]
        for i in range(1, len(intervals)):
            if time[0] <= intervals[i].start:
                heapq.heappop(time)
            heapq.heappush(time , intervals[i].end)
        return len(time)