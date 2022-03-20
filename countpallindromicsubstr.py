class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def countP(s, l, r):
            cur = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur +=1
                l -=1
                r +=1
            return cur
        
        for i in range(len(s)):
            res += countP(s, i, i)
            res += countP(s, i, i+1)
        return res

sol = Solution()
print(sol.countSubstrings("aaa"))
    