nums1 = [3,5,7]
m = 3 
nums2 = [4,10,14] 
n = 3

i = 0

while(m>0 and i<len(nums2)):
    if(nums1[m-1]>nums2[i]):
        nums1[m-1],nums2[i] = nums2[i],nums1[m-1] 
        i+=1
        m -=1
    else:
        m -=1

nums1.sort()
nums2.sort()
print(nums1 + nums2)