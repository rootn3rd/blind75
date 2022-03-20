from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2

            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
            
s = Solution()
arr = [4,5,6,7,0,1,2]
target = 0
print(s.search(arr,target))