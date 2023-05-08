nums = [1,3,4,2,2]

no = [0 for i in range(len(nums))] 

for i in range(len(nums)):
    if(no[nums[i]] == 0):
        no[nums[i]] = 1
    else:
        print( nums[i])

# TC: O(n) + O(n)
# SC: O(n)