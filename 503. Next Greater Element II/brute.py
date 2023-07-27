class Solution:
    def nextGreaterElements(self, nums):
        
  
        ans = [-1] * len(nums)
        
        for i in range(len(nums)):
            
            j = i+1
            
            while j < len(nums):
                if nums[j] > nums[i]:
                    ans[i] = nums[j]
                    break
                j +=1
            
            if j == len(nums):
                j = 0
                
                while j < i:
                    if nums[j] > nums[i]:
                        ans[i] = nums[j]
                        break
                    j +=1
            
        return ans