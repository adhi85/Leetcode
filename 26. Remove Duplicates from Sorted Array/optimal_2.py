nums =[-1,0,0,0,0,3,3]

j =1
for i in range(1,len(nums)):
    if(nums[i]!=nums[i-1]):
        nums[j]= nums[i]
        j+=1
        
print(nums[:j])
