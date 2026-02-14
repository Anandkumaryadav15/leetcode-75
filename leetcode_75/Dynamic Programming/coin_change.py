from typing import List

class Solution:
    """
    Problem: Coin Change
    
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
    
    Time Complexity: O(amount * len(coins))
    - We iterate through every amount from 1 to amount, and for each amount, we iterate through all coins.
    
    Space Complexity: O(amount)
    - We use a DP array of size amount + 1.
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] represents the minimum coins needed to make amount i
        # Initialize with a value larger than any possible answer (amount + 1)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Compute min coins for every amount from 1 to 'amount'
        for a in range(1, amount + 1):
            for c in coins:
                # If the coin value is not greater than the current amount we are trying to make
                if a - c >= 0:
                    # dp[a] = min(current_best, 1_coin + best_way_to_make_remainder)
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # If the value works out to be the infinity placeholder, it means we couldn't make that amount
        return dp[amount] if dp[amount] != float('inf') else -1
