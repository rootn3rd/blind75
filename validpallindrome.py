class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowedSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        l, r = 0, len(s)-1

        while l < r:
            while l < r and s[l] not in allowedSet:
                l += 1
            while l < r and s[r] not in allowedSet:
                r -= 1
            if s[r].lower() != s[l].lower():
                return False
            r -= 1
            l += 1

        return True


sol = Solution()
print(sol.isPalindrome('A man, a plan, a canal: Panama'))
