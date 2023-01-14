def maxIceCream(costs, coins):
        bucket = [0 for _ in range(max(costs) + 1)]
        for cost in costs:
            bucket[cost] += 1

        bars = 0
        for price, count in enumerate(bucket):
            if coins < price:
                break

            if count > 0:
                bars += min(count, coins // price)
                coins -= min(coins, price * count)

        return bars
