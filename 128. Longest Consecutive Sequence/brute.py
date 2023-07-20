class Solution:
    def longestConsecutive(self, nums):
        
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        
        maxc = 1
        count = 1
        
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                count = 1
            maxc = max(count,maxc)
                
        return maxc
    
# TC: O(NlogN)
# SC: O(1)