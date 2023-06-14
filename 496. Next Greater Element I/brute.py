nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
ans = []

for i in range(len(nums1)):
    j = 0
    while True:
        if nums2[j] == nums1[i]:
            break
        j += 1
    next = -1
    for k in range(j, len(nums2)):
        if nums2[k] > nums1[i]:
            next = nums2[k]
            break
    ans.append(next)

print(ans)

# TC:O(n^2)
