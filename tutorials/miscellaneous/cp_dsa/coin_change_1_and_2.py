class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    def coinChange2(self, coins: list[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        
        return dp[amount] if dp[amount] != float('inf') else 0
    
# Leetcode Coin Change problem: https://leetcode.com/problems/coin-change/

# Coin change 2 problem: https://leetcode.com/problems/coin-change-2/


# you have an infinite number of each coin denomination, 
# using a given set of coin denominations (coinChange) 
# and you want to find the minimum number of coins needed to make up the given amount. (in problem 1)
# and you want to find the total number of unique combinations that can make up the given amount. (in problem 2)

# Example usage:
solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  # Output: 3
print(solution.coinChange2([1, 2, 5], 11))  # Output: 11