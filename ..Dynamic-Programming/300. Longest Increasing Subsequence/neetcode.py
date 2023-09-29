class Solution:
    # TC: O(N^2)
    # SC: O(N)
    def lengthOfLIS(self, nums):
        n = len(nums)
        LIS = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


T = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(T.lengthOfLIS(nums))
