class Solution:
    def twoSum(self, nums, target: int):
        cache = {}
        for i, v in enumerate(nums):
            if v in cache:
                return [cache[v], i]
            cache[target - v] = i

        return []


s = Solution()
arr = [2, 7, 11, 15]
target = 9
print(s.twoSum(arr, target))


# Time O(n)
# Space O(n)