import sys
def minCoins(coins, M, V):
    dp = [sys.maxsize] * (V + 1)
 
    dp[0] = 0
 
    for i in range(1, V + 1):
        for j in range(M):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
 
    return dp[V] if dp[V] != sys.maxsize else -1
 
coins = [1, 2, 5]
M = len(coins)
V = 11

result = minCoins(coins, M, V)
print(f"Minimum number of coins required: {result}")
