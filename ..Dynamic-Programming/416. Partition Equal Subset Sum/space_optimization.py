class Solution:
    def canPartition(self, nums):

        N = len(nums)

        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        '''
            because it is dependent only on next and current row
            we just need only 2 rows and target+1 colums

            we just need to update the nextRow with currRow after every loop
            because it is coming backwards

        '''
        currRow = [False] * (target+1)
        nextRow = [False] * (target+1)
        currRow[0] = True
        nextRow[0] = True

        for indx in range(N-1, -1, -1):
            for trgt in range(target+1):

                include = 0
                if trgt-nums[indx] >= 0:
                    include = nextRow[trgt - nums[indx]]
                exclude = nextRow[trgt]

                currRow[trgt] = include or exclude
            # We have to use copy because python reference
            nextRow = currRow[:]

        return nextRow[target]


T = Solution()
# nums = [1, 2, 3, 5, 17, 6, 14, 12, 6]
nums = [1, 2, 5]

print(T.canPartition(nums))
