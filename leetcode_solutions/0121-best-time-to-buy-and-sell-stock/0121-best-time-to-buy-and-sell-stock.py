class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float("-Inf")
        buy_day = float("Inf")
        sell_day = 0
        
        for price in prices:
            buy_day = min(buy_day, price)
            sell_day = max(buy_day, price)
            
            max_profit = max(max_profit, sell_day - buy_day)
        return max_profit
        