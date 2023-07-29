class Solution:
    def search(self, nums, target: int) -> bool:
        l,r = 0, len(nums)-1
        
        while l<=r:
            
            # Shifting the duplicates
            while l<r and nums[l] == nums[l+1]:
                l +=1
            while l<r and nums[r] == nums[r-1]:
                r -=1
                
            m = (l+r) >> 1
            
            if nums[m] == target:
                return True
            
            elif nums[m] >= nums[l]:
                if target < nums[m] and target >= nums[l]:
                    r = m -1
                else:
                    l = m+1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        
        return False
                