class Solution:
    def lengthOfLIS(self, nums):

        # Space-Optimization
        # TC: O(N^2)
        # SC: O(N)

        n = len(nums)

        nextRow = [0] * (n+1)
        currRow = [0] * (n+1)

        for indx in range(n-1, -1, -1):
            for prev in range(indx-1, -2, -1):

                # Include
                include = 0
                if prev == -1 or nums[indx] > nums[prev]:
                    include = 1 + nextRow[indx+1]

                # Exclude
                exclude = 0 + nextRow[prev+1]

                currRow[prev+1] = max(include, exclude)

            nextRow = currRow

        return currRow[0]


T = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(T.lengthOfLIS(nums))
