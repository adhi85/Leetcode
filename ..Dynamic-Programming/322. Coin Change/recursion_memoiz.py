class Solution:
    def coinChange(self, coins, amount):
        dp = [-1] * (amount+1)
        ans = self.solveMem(coins,amount,dp)

        if ans != float("inf"):
            return ans
        return -1
    
    # TC: O(N * amount)
    # SC: O(amount)

    def solveMem(self,coins,amount,dp):
        if amount == 0:
            return 0
        
        if amount < 0:
            return float("inf")
        
        mini = float("inf")

        if dp[amount] != -1:
            return dp[amount]

        for i in range(len(coins)):
            ans = self.solveMem(coins,amount-coins[i],dp)

            if ans != float("inf"):
                mini = min(mini,1 + ans)

        dp[amount] = mini

        return dp[amount]

import time
start = time.time()

coins = [1,2,5]
amount = 11


T = Solution()

print(T.coinChange(coins,amount))

end = time.time()
print(start -end)