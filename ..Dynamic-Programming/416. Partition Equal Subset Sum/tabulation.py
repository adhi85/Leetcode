class Solution:
    def canPartition(self, nums):

        # TC: O(total*N)

        N = len(nums)
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        # N+1 because we are doing index+1 in loop
        dp = [[False for _ in range(target+1)] for _ in range(N + 1)]

        '''
            base case is target == 0:
                make it true
        '''
        # N+1 because we are doing index+1 in loop
        for i in range(N+1):
            dp[i][0] = True

        '''
            since Top down approach went 
                indx from 0-> N and
                target from target-> 0
            we'll have to reverse it in bottom-up approach
        '''

        for indx in range(N-1, -1, -1):
            for trgt in range(target+1):
                # make the same relations but with dp

                include = False
                if trgt - nums[indx] >= 0:
                    # N+1 because we are doing index+1 in loop
                    include = dp[indx+1][trgt-nums[indx]]
                exclude = dp[indx+1][trgt]

                dp[indx][trgt] = include or exclude

        return dp[indx][target]


T = Solution()
nums = [1, 2, 3, 5, 17, 6, 14, 12, 6]

print(T.canPartition(nums))
