from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1, rob2 = 0, 0
            for a in arr:
                temp = max(rob1 + a, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0])


sol = Solution()
print(sol.rob([2, 3, 2]))
