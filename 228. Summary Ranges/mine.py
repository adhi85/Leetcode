class Solution:
    def summaryRanges(self, nums):
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and (nums[i] + 1 == nums[i + 1]):
                i += 1

            if nums[i] != start:
                temp = str(start) + "->" + str(nums[i])
            else:
                temp = str(nums[i])

            ans.append(temp)
            i += 1

        return ans

# TC : O(N)
# SC : O(1)