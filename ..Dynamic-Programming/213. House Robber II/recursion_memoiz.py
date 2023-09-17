class Solution:
    def rob(self, nums):

        dp1 = [-1] * (len(nums)+1)
        dp2 = [-1] * (len(nums)+1)

        return max(nums[0], self.solveMem(nums[1:], 0, dp1), self.solveMem(nums[:-1], 0, dp2))

    def solveMem(self, nums, n, dp):

        if n >= len(nums):
            return 0

        if n == len(nums) - 1:
            return nums[-1]

        if dp[n] != -1:
            return dp[n]

        include = self.solveMem(nums, n+2, dp) + nums[n]
        exclude = self.solveMem(nums, n+1, dp) + 0

        dp[n] = max(include, exclude)

        return dp[n]

import time
start = time.time()

nums = [1, 2, 3, 1]

T = Solution()

print(T.rob(nums))

end = time.time()
print(f"Time: {start -end}")