def removeDuplicates(nums):
    ass = set()
    

    for i in nums:
        ass.add(i)

    j = 0
    for i in ass:
        nums[j] = i
        j +=1
    
    nums[:j] = sorted(nums[:j])
    
    return j

nums =[-1,0,0,0,0,3,3]

print(nums[:removeDuplicates(nums)])

# TC: O(N)
# SC: O(N)