nums = [1,3,4,2,2]

nums.sort()

for i in range(len(nums)-1):
    if(nums[i] == nums[i+1]):
        print (nums[i])

# TC: O(nlogn) + O(n)
#but modifies the array