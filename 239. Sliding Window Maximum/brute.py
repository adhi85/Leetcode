def maxSlidingWindow(self, nums, k):
    if k == 1:
        return nums
    low = 0
    high = k - 1

    ans = []

    while high < len(nums):
        ans.append(max(nums[low:high+1]))

        low += 1
        high += 1
    return ans

# TC: O(N*K)
# SC : O(1)