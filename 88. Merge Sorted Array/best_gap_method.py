nums1 = [3,5,7]
m = 3 
nums2 = [4,10,14] 
n = 3

length = (m+n)
gap = length//2 + (length % 2)

while gap > 0 :
    left = 0
    right = left + gap 
    
    while(right < m+n):
        if( left< m and right >= m ):
            if(nums1[left] > nums2[right-m]):
                nums1[left], nums2[right-m] = nums2[right-m], nums1[left]
        elif (left>=m):
            if(nums2[left-m] > nums2[right-m]):
                nums2[left-m], nums2[right-m] = nums2[right-m], nums2[left-m]
        else:
            if(nums1[left] > nums1[right]):
                nums1[left], nums1[right] = nums1[right], nums1[left]
        left+=1
        right+=1
    if gap == 1:
        break 
    else:
        gap = gap//2 + (gap%2)
    
# TC: O(log2(m+n)) + O(m+n) approx
# Sc : O(1)
print(nums1 + nums2)