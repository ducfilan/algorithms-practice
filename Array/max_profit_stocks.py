# This problem was recently asked by Apple:
#
# You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.
#
# For example: [9, 11, 8, 5, 7, 10]
#
# Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).
#
# Here's your starting point:
#
# def buy_and_sell(arr):
#   #Fill this in.
#
# print buy_and_sell([9, 11, 8, 5, 7, 10])
# # 5


def buy_and_sell(prices):
    if not prices or len(prices) < 2:
        return 0

    p1, p2 = 0, 1
    max_profit = 0
    while p2 < len(prices):
        max_profit = max(max_profit, prices[p2 - 1] - prices[p1])
        if prices[p1] >= prices[p2]:
            p1 = p2

        p2 += 1
    else:
        max_profit = max(max_profit, prices[p2 - 1] - prices[p1])

    return max_profit


print(buy_and_sell([9, 11, 8, 5, 7, 10]) == 5)
print(buy_and_sell([9, 11]) == 2)
print(buy_and_sell([99, 11]) == 0)
print(buy_and_sell([9]) == 0)
print(buy_and_sell([]) == 0)
print(buy_and_sell([3, 5, 3, 4]) == 2)
print(buy_and_sell([7, 1, 5, 3, 6, 4]) == 5)
