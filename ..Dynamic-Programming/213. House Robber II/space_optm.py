class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        return max(nums[0], self.solveOpt(nums[1:]), self.solveOpt(nums[:-1]))

    def solveOpt(self, nums):

        prev2 = 0
        prev1 = nums[0]

        for i in range(1, len(nums)):
            include = prev2 + nums[i]
            exclude = prev1 + 0

            ans = max(include, exclude)

            prev2 = prev1
            prev1 = ans

        return prev1
