from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) -1
        while left<right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
            mid = (left + right)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1
        return res


s = Solution()
arr = [3,4,5,6,7,1,2]
print(s.findMin(arr))

# Time: O(logn)
# Space: O(1)




