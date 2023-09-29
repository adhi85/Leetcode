import bisect


'''
    # DP With Binary search
    
    the ans we get maynot be the correct sequence but since we dont need the 
    subsequence and only the length we'll replace the elements
    ans = [10]
    ans = [9] 9 < 10
    ans = [2] 2 < 10
    !!! ans = [2,5] 5 > 2
    ans = [2,3] 3 < 5
    !!! ans = [2,3,7] 7 > 3
    !!! ans = [2,3,7,101] 101 > 7
    ans = [2,3,18,101] 18 < 101
'''


class Solution:
    # TC : O(NlogN)
    # SC : O(len(ans))
    def lengthOfLIS(self, nums):
        ans = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                index = bisect.bisect_left(ans, nums[i])
                ans[index] = nums[i]
        return len(ans)


T = Solution()

nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(T.lengthOfLIS(nums))
