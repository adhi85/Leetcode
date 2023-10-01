class Solution:
    def canPartition(self, nums):

        # TOP-DOWN APPROACH
        # TC: O(target*N)

        N = len(nums)

        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [[-1 for _ in range(target+1)] for _ in range(N)]

        def solveMem(indx, target):
            if target == 0:
                return True

            if indx >= len(nums) or target < 0:
                return False

            if dp[indx][target] != -1:
                return dp[indx][target]

            include = solveMem(indx+1, target-nums[indx])
            exclude = solveMem(indx+1, target-0)

            dp[indx][target] = include or exclude

            return dp[indx][target]

        return solveMem(0, target)


T = Solution()
nums = [1, 2, 3, 5, 17, 6, 14, 12, 6]

print(T.canPartition(nums))
