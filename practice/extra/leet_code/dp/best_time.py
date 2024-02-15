# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def profit(T):
    n = len(T)
    res = 0
    buy = T[0]
    for i in range(1, n):
        if T[i] < buy:
            buy = T[i]
        if T[i] - buy > res:
            res = T[i] - buy
    return res

prices = [7, 1, 5, 3, 6, 4]
# print(profit(prices))

