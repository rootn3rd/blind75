from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]) ,  max(intervals[i][1], newInterval[1]) ]
        res.append(newInterval)
        return res


sol = Solution()
arr =[[1,2],[3,5],[6,7],[8,10],[12,16]]
newInt = [4,8]
print(sol.insert(arr, newInt))
