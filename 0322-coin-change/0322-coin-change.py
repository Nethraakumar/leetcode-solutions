class Solution:
    def coinChange(self, coins, amount):
        # dp[i] = minimum coins needed for amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                if dp[x - coin] != float('inf'):
                    dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1