class Solution:
    def nextGreaterElements(self, nums):

        stack = []
        ans = [-1] * len(nums)

        for i in range(len(nums) * 2):
            i %= len(nums)

            while stack and nums[i] > nums[stack[-1]]:
                indx = stack.pop()
                ans[indx] = nums[i]

            stack.append(i)

        return ans
