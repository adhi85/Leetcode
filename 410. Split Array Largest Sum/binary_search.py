class Solution:
    def splitArray(self, nums, k) -> int:

        def isFeasible(sum_limit):
            curr_kval = 1
            curr_sum = 0

            for n in nums:
                curr_sum += n

                if curr_sum > sum_limit:
                    curr_sum = n
                    curr_kval += 1

                    if curr_kval > k:
                        return False
            return True

        left, right = max(nums), sum(nums)

        while left < right:

            mid = (left+right) >> 1

            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
