from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue

            tmp = curMax*n
            curMax = max(n * curMax, n * curMin, n)
            curMin = max(tmp, n * curMin, n)
            res = max(res, curMax, curMin)

        return res

s = Solution()
arr = [2,3,-2,4]
print(s.maxProduct(arr))