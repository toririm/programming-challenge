import heapq

t = int(input())


def get_min(sell):
    if len(sell) > 0:
        price, amount = sell[0]
        return price, amount
    return None, None


for _ in range(t):
    n = int(input())
    buy = []
    sell = []
    orders = [input().split() for _ in range(n)]
    orders = [
        {
            k: v
            for k, v in zip(
                ["type", "amount", "price"], [order[0], int(order[1]), int(order[4])]
            )
        }
        for order in orders
    ]
    s = "-"
    for order in orders:
        if order["type"] == "buy":
            heapq.heappush(buy, (-order["price"], order["amount"]))
        else:
            heapq.heappush(sell, (order["price"], order["amount"]))
        a, b = "-", "-"
        buy_price, buy_amount = get_min(buy)
        sell_price, sell_amount = get_min(sell)
        while buy and sell and buy_price and sell_price:
            buy_price, buy_amount = get_min(buy)
            sell_price, sell_amount = get_min(sell)
            if -buy_price >= sell_price:
                s = sell_price
                if buy_amount > sell_amount:
                    heapq.heappop(buy)
                    heapq.heappop(sell)
                    heapq.heappush(buy, (buy_price, buy_amount - sell_amount))
                elif buy_amount < sell_amount:
                    heapq.heappop(buy)
                    heapq.heappop(sell)
                    heapq.heappush(sell, (sell_price, sell_amount - buy_amount))
                else:
                    heapq.heappop(buy)
                    heapq.heappop(sell)
            else:
                break
        buy_price, buy_amount = get_min(buy)
        sell_price, sell_amount = get_min(sell)
        if buy_price:
            b = -buy_price
        if sell_price:
            a = sell_price
        print(f"{a} {b} {s}")
