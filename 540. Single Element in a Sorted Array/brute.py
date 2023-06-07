nums = [1,1,2,3,3,4,4,8,8]

if len(nums) == 1:
    print(nums[0])
for i in range(0,len(nums) ,2):
    if i == len(nums)-1:
        print(nums[i])
        break
    if nums[i] != nums[i+1]:
        print( nums[i])
        break
    
# TC: O(N/2)
