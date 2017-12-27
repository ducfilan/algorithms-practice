# Given a target amount n and a list (array) of distinct coin values,
# what's the fewest coins needed to make the change amount.
#
# For example:
#
# If n = 10 and coins = [1,5,10]. Then there are 4 possible ways to make change:
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
#
# 5 + 1 + 1 + 1 + 1 + 1
#
# 5 + 5
#
# 10
#
# With 1 coin being the minimum amount.


def coin_change(target, coins, cache={}):
    min_coins = target

    if target in cache:
        return cache[target]

    if target in coins:
        return 1

    for coin in filter(lambda x: x <= target, coins):
        num_coins = 1 + coin_change(target - coin, coins)
        min_coins = min(num_coins, min_coins)

    cache[target] = min_coins
    return min_coins
