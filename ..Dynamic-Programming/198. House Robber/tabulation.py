import time
# TC: O(N)
# SC: O(N)

class Solution:
    def rob(self, nums):
        return self.solveTab(nums)

    def solveTab(self, nums):
        n = len(nums)

        dp = [0] * (n+1)
        dp[0] = nums[0]

        for i in range(1, n):
            include = dp[i-2] + nums[i]
            exclude = dp[i-1] + 0

            dp[i] = max(include, exclude)

        return dp[n-1]


start = time.time()

nums = [1, 2, 3, 1]

T = Solution()

print(T.rob(nums))

end = time.time()
print(f"Time: {start -end}")
