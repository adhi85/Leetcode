class Solution:
    def maximumUniqueSubarray(self, nums):
        
        hashset = set()
        
        l = 0
        s,maxs = 0,0
        
        for r in range(len(nums)):
            while nums[r] in hashset:
                hashset.remove(nums[l])
                s -= nums[l]
                l +=1
            
            hashset.add(nums[r])
            s +=nums[r]
            
            maxs = max(maxs,s)
        
        return maxs