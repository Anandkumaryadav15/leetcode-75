from typing import List

class Solution:
    """
    Problem: Best Time to Buy and Sell Stock
    
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    
    Time Complexity: O(n)
    - Only a single pass is needed.
    
    Space Complexity: O(1)
    - Only two variables are used.
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Initialize min_price to infinity and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price
            # Else, check if selling at current price yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
