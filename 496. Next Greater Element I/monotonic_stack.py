class Solution:
    # Solution using less space scroll down below
    def nextGreaterElement(self, nums1, nums2):

        hashmap = {v: i for i, v in enumerate(nums1)}
        stack = []
        ans = [-1] * len(nums1)

        for i, v in enumerate(nums2):
            while stack and v > stack[-1][1]:
                ind, val = stack.pop()
                ans[hashmap[val]] = v

            if v in hashmap:
                stack.append((i, v))

        return ans

# TC:O(N)
# SC:O(N)

        
# hashmap = {v:i for i,v in enumerate(nums1)}
# stack = []
# ans = [-1] * len(nums1)

# for i in range(len(nums2)):
#     while stack and nums2[i] > stack[-1]:
#         val = stack.pop()
#         ans[hashmap[val]] = nums2[i]
    
#     if nums2[i] in hashmap:
#         stack.append(nums2[i])
        
# return ans
