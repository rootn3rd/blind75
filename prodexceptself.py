from sys import prefix
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lArr = [1]* len(nums)
        rArr = [1]* len(nums)
        
        for i in range(1, len(nums)):
            lArr[i] = lArr[i-1] * nums[i-1]
        
        for i in range(len(nums) -2, -1, -1):
            rArr[i] = rArr[i+1] * nums[i+1]
        
        return [a*b for a, b in zip(lArr, rArr)]
    # Time - O(n)
    # Space - O(n)

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        
        res = [1]* len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

    # Time - O(n)
    # Space - O(1)
