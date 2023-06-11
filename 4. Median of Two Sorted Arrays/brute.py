def findMedianSortedArrays(self, nums1, nums2):
    
    nums1 = nums1 + nums2

    nums1.sort()
    
    if len(nums1) % 2 == 0:
        return (nums1[(len(nums1)//2)-1] + nums1[(len(nums1)//2)])/2
    
    return nums1[len(nums1)//2]

# TC: O(N + M) + O((N+M)log(N+M))
# SC : O(1)