import time

# TC: O(N)
# SC: O(1)
class Solution:
    def rob(self, nums):

        n = len(nums)

        prev1 = nums[0]
        prev2 = 0

        for i in range(1, n):
            include = prev2 + nums[i]
            exclude = prev1 + 0

            ans = max(include, exclude)

            prev2 = prev1
            prev1 = ans

        return prev1

start = time.time()

nums = [1, 2, 3, 1]

T = Solution()

print(T.rob(nums))

end = time.time()
print(f"Time: {start -end}")
