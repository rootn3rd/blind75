from typing import List
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda i: i[0])

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                return False
            prevEnd = end
        return True




sol = Solution()
intv=[(0,30),(5,10),(15,20)]
print(sol.can_attend_meetings(intv))