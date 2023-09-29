class Solution:
    def lengthOfLIS(self, nums):

        # Bottom-UP Approach
        # TC: O(N^2)
        # SC: O(N^2)

        n = len(nums)
        dp = [[0] * (n+1)] * (n+1)

        for indx in range(n-1, -1, -1):
            for prev in range(indx-1, -2, -1):

                # include
                include = 0
                if prev == -1 or nums[indx] > nums[prev]:
                    include = 1 + dp[indx+1][indx+1]

                exclude = 0 + dp[indx+1][prev+1]

                dp[indx][prev+1] = max(include, exclude)

        return dp[0][0]


T = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(T.lengthOfLIS(nums))
