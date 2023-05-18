class Solution:
    def containsDuplicate(self, nums):
        counter = {}

        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i],0)
            if counter[nums[i]] > 1:
                return True
        return False
    
# TC: O(n)
# SC: O(n)