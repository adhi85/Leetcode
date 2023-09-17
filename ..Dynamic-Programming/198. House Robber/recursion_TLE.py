import time


class Solution:
    def rob(self, nums):
        n = len(nums)
        return self.solveRec(nums, n-1)

    def solveRec(self, nums, indx):
        # We are trying to com from the last index to first
        # Base case
        if indx < 0:
            return 0

        # We have to return the 0th index if we reach 0
        if indx == 0:
            return nums[0]

        '''
        We can either include an element or exclude that element
        '''
        # For including we cant take the nearest element then so give index - 2 i.e come down two steps
        include = self.solveRec(nums, indx-2) + nums[indx]
        exclude = self.solveRec(nums, indx-1) + 0

        return max(include, exclude)


start = time.time()

nums = [1, 2, 3, 1]

T = Solution()

print(T.rob(nums))

end = time.time()
print(f"Time: {start -end}")
