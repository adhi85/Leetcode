class Solution:
    def canPartition(self, nums):

        # TLE

        total = sum(nums)

        if total % 2:
            return False

        total = total >> 1

        def help(indx, smm):
            if smm == total:
                return True

            if smm > total or indx >= len(nums):
                return False

            return help(indx+1, smm+nums[indx]) or help(indx+1, smm)

        return help(0, 0)


T = Solution()
nums = [1, 2, 3, 5, 17, 6, 14, 12, 6]

print(T.canPartition(nums))
