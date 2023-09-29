class Solution:
    # TC: O(2^N)
    def lengthOfLIS(self, nums):

        def solveRec(indx, prev):
            if indx == len(nums):
                return 0

            # Include the nums[indx] if condition satisfies
            include = 0

            # If prev == -1 means first index and include only if increasing subsequence
            if prev == -1 or nums[indx] > nums[prev]:
                include = 1 + solveRec(indx+1, indx)  # prev becomes curr_indx

            # Exclude
            exclude = 0 + solveRec(indx+1, prev)

            return max(include, exclude)

        return solveRec(0, -1)


T = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(T.lengthOfLIS(nums))
