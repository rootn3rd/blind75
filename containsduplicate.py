class Solution:
    def containsDuplicate(self, nums) -> bool:
        cache = set()
        for n in nums:
            if n in cache:
                return True
            cache.add(n)
        return False

            
s = Solution()
arr = [1,7,1,5,3,6,4]
print(s.containsDuplicate(arr))

# Time: O(n)
# Space: O(1)