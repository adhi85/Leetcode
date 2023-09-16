class Solution:
    def coinChange(self,coins,amount):

        return self.solveTab(coins,amount)

    # TC: O(N * amount)
    # SC: O(amount)

    '''
    dp[i] depends on dp[i-coin]
    so cant do space optimization
    '''

    def solveTab(self,coins,amount):
        dp = [amount +1] * (amount+1)

        dp[0] = 0

        for amt in range(amount+1):
            # I am Trying to loop through coins and find difference between each coin and current amt
            for c in coins:
                # Only find if >=0 because if negative that coin cant be taken
                if amt-c >=0:
                    """ its like if amt == 5 and c = 3 dp[5] = 1 + dp[2] => we would have already found 
                        n.o of coins for the amount amt-coin i.e dp[2]
                        we need to find n.o of min coin when it is amount i.e  dp[x] at x == amount
                    """
                    dp[amt] = min(dp[amt],1 + dp[amt-c])

        return dp[amount] if dp[amount] != amount +1 else -1

import time
start = time.time()

coins = [1, 2, 5]
amount = 11

T = Solution()

print(T.coinChange(coins,amount))

end = time.time()
print(start -end)