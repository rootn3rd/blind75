class Solution:
    def maxProfit(self, prices) -> int:
        l, r = 0, 1 
        maxProfit = 0
        while r < len(prices):
            
            if prices[l] < prices[r]:
                profit =  prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
            
s = Solution()
arr = [7,1,5,3,6,4]
print(s.maxProfit(arr))

# Time: O(n)
# Space: O(1)