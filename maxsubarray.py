from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

    def maxSubArray2(self, nums: List[int]) -> int:

        res = nums[:]
        for i in range(1, len(nums)):
            res[i] = max(res[i], res[i-1]+ nums[i])
        return max(res)

s = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(arr))

