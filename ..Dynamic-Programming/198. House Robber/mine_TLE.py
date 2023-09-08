class Solution:
    def rob(self, nums):

        ans = [float("-inf")]

        def money(indx, total):

            if indx >= len(nums):
                ans[0] = max(total, ans[0])
                return

            for i in range(indx, len(nums)):
                money(i+2, total+nums[i])

        money(0, 0)
        return ans[0]
