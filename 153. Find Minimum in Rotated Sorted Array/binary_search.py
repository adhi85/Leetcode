class Solution:
    def findMin(self, nums):

        l,r = 0 , len(nums)-1
        
        ans = nums[0]
        
        while l <=r:
            m = (l+r) >> 1
            
            ans = min(ans,nums[m])
            
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m-1
        return ans
            
            
            

        
        