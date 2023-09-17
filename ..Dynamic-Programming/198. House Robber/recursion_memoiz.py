import time

# TC: O(N)
# SC: O(N)

class Solution:
    def rob(self, nums):
        n = len(nums)

        dp = [-1] * (n+1)

        return self.solveMem(nums,n-1,dp)

    def solveMem(self, nums, indx, dp):

        # Base cases
        if indx < 0:
            return 0

        if indx == 0:
            return nums[0]

        # Step 3: return if already in dp
        if dp[indx] != -1:
            return dp[indx]

        inlcude = self.solveMem(nums, indx-2, dp) + nums[indx]
        exclude = self.solveMem(nums, indx-1, dp) + 0

        # Step 2 : store in dp
        dp[indx] = max(inlcude, exclude)

        return dp[indx]

start = time.time()

nums = [1, 2, 3, 1]

T = Solution()

print(T.rob(nums))

end = time.time()
print(f"Time: {start -end}")
