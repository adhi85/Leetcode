import time


class Solution:
    def rob(self, nums):
        return max(nums[0], self.solveRec(nums[1:], 0), self.solveRec(nums[:-1], 0))

    def solveRec(self, nums, n):
        if n >= len(nums):
            return 0

        if n == len(nums)-1:
            return nums[-1]

        include = self.solveRec(nums, n+2) + nums[n]
        exclude = self.solveRec(nums, n+1) + 0

        return max(include, exclude)


start = time.time()

nums = [1, 2, 3, 1]

T = Solution()

print(T.rob(nums))

end = time.time()
print(f"Time: {start -end}")
