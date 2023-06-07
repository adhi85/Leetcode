
nums = [1,1,2,3,3,4,4,8,8]

xor = nums[0]

for i in range(1,len(nums)):
    xor ^= nums[i]
    
print(xor)