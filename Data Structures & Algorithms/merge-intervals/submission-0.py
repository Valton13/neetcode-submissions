class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair :pair[0])
        res = [intervals[0]]
        for i,j in intervals:
            out = res[-1][1]
            if out >= i:
                res[-1][1] = max(out, j )
            else:
                res.append([i,j])
        return res