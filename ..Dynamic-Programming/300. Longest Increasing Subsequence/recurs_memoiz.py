class Solution:
    # TC: O(N^2)
    # SC: O(N^2)
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[-1] * (n+1)] * (n+1)

        def solveMem(indx, prev):
            if indx == len(nums):
                return 0

            if dp[indx][prev+1] != -1:
                return dp[indx][prev+1]

            # Include
            include = 0
            if prev == -1 or nums[indx] > nums[prev]:
                include = 1 + solveMem(indx+1, indx)

            # Exclude
            exclude = 0 + solveMem(indx+1, prev)

            dp[indx][prev+1] = max(include, exclude)

            return dp[indx][prev+1]

        return solveMem(0, -1)


T = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(T.lengthOfLIS(nums))
