from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res


sol = Solution()
arr = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(sol.missingNumber(arr))
