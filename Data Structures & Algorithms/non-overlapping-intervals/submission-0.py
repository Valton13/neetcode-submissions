class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        end = intervals[0][1]
        for i , j in intervals[1:]:
            if i>=end:
                end = j
            else:
                res += 1
                end = min(j,end)
        return res