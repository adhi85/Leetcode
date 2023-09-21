class Solution:
    def maxProduct(self, nums):

        if len(nums) == 1:
            return nums[0]

        ans = float("-inf")

        for i in range(len(nums)-1):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                temp *= nums[j]
                ans = max(temp, ans)

        return max(ans, max(nums))
