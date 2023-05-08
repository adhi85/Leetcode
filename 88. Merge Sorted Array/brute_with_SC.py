nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6] 
n = 3

ans = []
i=j=0

while(i<m and j <n):
    if(nums1[i]<=nums2[j]):
        ans.append(nums1[i])
        i+=1
    else:
        ans.append(nums2[j])
        j+=1
while i<m:
    ans.append(nums1[i])
    i+=1
while j<n:
    ans.append(nums2[j])
    j+=1

for i in range(m+n):
    nums1[i] = ans[i]

# TC: O(m+n) + O(m+n)
# SC: O(m+n)
print(nums1)
