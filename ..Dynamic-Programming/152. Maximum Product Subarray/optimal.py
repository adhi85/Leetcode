class Solution:
    def maxProduct(self, nums):
        ans = max(nums)

        curMax = 1
        curMin = 1

        '''
        We are trying to find the max and min for every index 
        min because if there is two negative numbers it can become postitve or change 
        '''

        for i in nums:
            
            # It will work even without this
            # if i == 0:
            #     curMax = 1
            #     curMin = 1

            temp = curMax

            curMax = max(curMax*i , curMin* i, i)
            curMin = min(temp*i , curMin* i, i)
            
            ans = max(ans,curMax)

        return ans
    
T = Solution()

nums = [2,3,-2,4]
print(T.maxProduct(nums))