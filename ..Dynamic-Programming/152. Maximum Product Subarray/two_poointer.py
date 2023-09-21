class Solution:
    def maxProduct(self, nums):

        # TC: O(N)
        # SC: O(N)

        l = r = 1

        ans = max(nums)
        n = len(nums)
        
        for i in range(n):
            
            if l == 0:
                l = 1
            if r == 0:
                r = 1

            l *= nums[i]
            r *= nums[n-i-1]

            ans = max(ans,l,r)

        return ans
    
T = Solution()
nums = [2,3,-2,4]

print(T.maxProduct(nums))