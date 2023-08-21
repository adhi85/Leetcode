cost = [10, 15, 20]
n = len(cost)

# TC:O(N) Iterative
# SC:O(N)
dp = []

for i in range(n):
    if i <= 1:
        dp.append(cost[i])
        continue

    dp.append(cost[i] + min(dp[i-1], dp[i-2]))

print(min(dp[n-1], dp[n-2]))
