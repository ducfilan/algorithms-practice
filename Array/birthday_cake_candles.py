# You are in-charge of the cake for your niece's birthday and have decided the cake will have one candle for each year
# of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to
# find out how many candles she can successfully blow out.
# For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 3, 2, 1, 3, she will be
# able to blow out 2 candles successfully, since the tallest candle is of height 3 and there are 2 such candles.
# Complete the function birthdayCakeCandles that takes your niece's age and an integer array containing height of each
# candle as input, and return the number of candles she can successfully blow out.
# 
# Sample Input 0
# 4
# 3 2 1 3
# Sample Output 0
# 2


def birthday_cake_candles(n, ar):
    tallest = 0
    tallest_count = 1

    for candle in ar:
        if candle > tallest:
            tallest = candle
            tallest_count = 1
        elif candle == tallest:
            tallest_count += 1

    return tallest_count
