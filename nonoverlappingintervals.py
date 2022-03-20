from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res +=1
                prevEnd = min(prevEnd, end)
        return res

sol = Solution()
intev = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intev))