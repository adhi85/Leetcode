def findMedianSortedArrays(self, nums1, nums2):
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    n1 = len(nums1)
    n2 = len(nums2)
    
    if not nums1:
        if n2 % 2 == 1:
            return nums2[n2//2]
        else:
            n2 -= 1
            return (nums2[n2//2] + nums2[n2//2 + 1]) /2
    
    low = 0
    high = n1 
    
    while low<=high:
        cut1 = (low + high) >> 1
        cut2 = (n1+n2+1) // 2 - cut1
        
        l1 = -1 * (10**6) if cut1 == 0 else nums1[cut1-1] 
        l2 = -1 * (10**6) if cut2 == 0 else nums2[cut2-1]
        
        r1 = 10**6 if cut1 == n1 else nums1[cut1]
        r2 = 10**6 if cut2 == n2 else nums2[cut2] 
            
        if l1 <= r2 and l2 <= r1:
            if (n1+n2) % 2 == 0:
                lmax = max(l1,l2)
                rmin = min(r1,r2)
                
                return (lmax+rmin) / 2
            else:
                return max(l1,l2)
        elif l1 > r2 :
            high = cut1 -1 
        else:
            low = cut1 + 1

# TC: O(log(n1+n2))
# SC: O(1)