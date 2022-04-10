def maxProfit(prices) -> int:
    max_profit = sell_day = 0
    buy_day = float('inf')

    for price in prices:
        buy_day = min(buy_day, price)
        sell_day = max(buy_day, price)
        max_profit = max(max_profit, sell_day - buy_day)

    return max_profit


##############################################################
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
# print(maxProfit([7, 6, 4, 3, 1]))
