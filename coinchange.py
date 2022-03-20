from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a-c], dp[a])
        return dp[-1] if dp[-1] != amount+1 else 0


sol = Solution()
inputA = [1, 3, 4]
amt = 7
print(sol.coinChange(inputA, amt))
