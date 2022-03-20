class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            n = n & (n -1)
            res +=1
        return res

sol = Solution()
inputV = 0o000000000000000000000000001011
print(sol.hammingWeight(inputV))
print(sol.hammingWeight2(inputV))
