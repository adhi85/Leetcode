nums = [1,2,3]

index = -1

for i in range(len(nums)-2,-1,-1):  #TC: O(n)
    if(nums[i]<nums[i+1]):
        index =i
        break
if index == -1:
    nums.reverse()                  
else:
    for i in range(len(nums)-1,index,-1):       #TC: O(n)
        if nums[i] > nums[index]:
            nums[i],nums[index] = nums[index],nums[i]
            break
    nums[index+1:] = reversed(nums[index+1:])       #TC: O(n)

# Total TC: O(3n)
print(nums)