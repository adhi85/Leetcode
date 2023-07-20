class Solution:
    def longestConsecutive(self, nums):
        
        x = set(nums)
        largest = 0
        
        for i in nums:
            if i-1 not in x:
                count = 0
                while (i + count) in x:
                    count +=1
                largest = max(count,largest)
                        
        return largest
    
# TC: O(N)
# SC: O(N)