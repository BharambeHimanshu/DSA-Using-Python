# Best time to buy abd sell stock
# Leetcode 121  (Easy Level)

# Brute force  TC -> o(n(n+1))//2    SC -> o(1)
price = [7, 2, 1, 5, 6, 4, 8]

def maxprofit(price):

    n = len(price)
    max_profit = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if price[j] > price[i]:
                profit = price[j] - price[i]
                max_profit = max(max_profit, profit)
    return max_profit

print(maxprofit(price))


# Optimal Solution  TC -> o(n)   SC -> o(1)

price = [7, 2, 1, 5, 6, 4, 8]

def maximumprofit(price):
    max_profit = 0
    min_price = float("inf")
    for i in range(0,len(price)):
        min_price = min(min_price, price[i])
        max_profit = max(max_profit, price[i] - min_price)
    return max_profit

print(maximumprofit(price))