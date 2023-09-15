class Solution:
    def coinChange(self, coins, amount: int) -> int:

        ans = [float("inf")]
        coins.sort()

        def solve(length, total):

            if total == amount:
                ans[0] = min(length, ans[0])
                return

            if ans[0] != float("inf"):
                return

            if total > amount:
                return

            for i in range(len(coins)-1, -1, -1):
                length += 1
                solve(length, total+coins[i])
                length -= 1

        solve(0, 0)

        if ans[0] != float("inf"):
            return ans[0]
        else:
            return -1
