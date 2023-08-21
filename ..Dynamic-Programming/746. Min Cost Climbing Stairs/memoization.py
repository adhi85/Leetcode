cost = [10,15,20]
n = len(cost)
dp = [-1] * (n+1)

# TC: O(N)
# SC: O(N)
def minCost(step):
    if step == 0:
        return cost[0]
    if step == 1:
        return cost[1]
    
    if dp[step] != -1:
        return dp[step]
    
    dp[step] = cost[step] + min(minCost(step-1), minCost(step-2))

    return dp[step]

ans = min(minCost(n-1),minCost(n-2))

print(ans)