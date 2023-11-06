def max_profit_stock(prices):
    max_profit = 0
    buy_day = 0
    sell_day = 0
    min_price = prices[0]
    result = []

    for i in range(1, len(prices)):
        if prices[i] < prices[i - 1]:
            if prices[i - 1] - min_price > max_profit:
                max_profit = prices[i - 1] - min_price
                result.append((buy_day + 1, sell_day + 1, max_profit))

            min_price = prices[i]
            buy_day = i
        sell_day = i

    if prices[sell_day] - min_price > max_profit:
        max_profit = prices[sell_day] - min_price
        result.append((buy_day + 1, sell_day + 1, max_profit))

    output = ""
    for buy, sell, profit in result:
        output += f"Buy stock on {buy}th day ({prices[buy - 1]})\n" \
                  f"Sell stock on {sell}th day ({prices[sell - 1]})\n"
    total_profit = sum(profit for _, _, profit in result)
    return output, total_profit

stock_prices = [100, 180, 260, 310, 40, 535, 695]
res, tp = max_profit_stock(stock_prices)
print(res)
print(f"Total Profit: {tp}")
