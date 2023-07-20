class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        ans = []
        a = 0
        
        for a in range(len(nums)):
            if a > 0 and nums[a-1] == nums[a]:
                continue
            
            l = a+1
            r = len(nums) -1
            
            while l < r:
                threesum = nums[l] + nums[r] + nums[a]
                
                if threesum > 0:
                    r -=1
                elif threesum < 0 :
                    l+=1
                else:
                    ans.append([nums[a],nums[l],nums[r]])
                    l +=1
                    while nums[l]==nums[l-1] and l<r:
                        l +=1
            
        return ans