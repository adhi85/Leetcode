class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        hashmap = {}
        
        for i,v in enumerate(nums1):
            hashmap[v] = i
        ans = [-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] in hashmap and i < len(nums2)-1:
                j = i
                
                while j < len(nums2)-1:
                    j +=1
                    if nums2[j] > nums2[i]:
                        ans[hashmap[nums2[i]]] = nums2[j]
                        break
                          
        return ans