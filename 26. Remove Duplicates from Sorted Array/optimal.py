def removeDuplicates(nums):
    i = 0
    j = 1
    while j<len(nums):
        if nums[j] != nums[i]:
            nums[i+1] = nums[j]
            i +=1
        j +=1
    return (i+1)

nums =[-1,0,0,0,0,3,3]

print(nums[:removeDuplicates(nums)])

# TC: O(N)
# SC: O(1)