# TC: Exponential

class Solution:
    def coinChange(self, coins, amount):
        ans = self.solveRec(coins,amount)

        if ans != float("inf"):
            return ans
        return -1

    def solveRec(self, coins, amount):
        if amount < 0:
            return float("inf")
        
        if amount == 0:
            return 0

        mini = float("inf")


        for i in range(len(coins)):

            ans = self.solveRec(coins,amount-coins[i])
            if ans != float("inf"):
                mini = min(mini,1+ ans)

        return mini

import time
start = time.time()

coins = [1, 2, 5]
amount = 11

T = Solution()

print(T.coinChange(coins,amount))

end = time.time()
print(start -end)