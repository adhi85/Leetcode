nums = [5,4,-1,7,8]
maxl = min(nums)
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum +=nums[j]
        if(sum>maxl):
            maxl = sum

# Total TC: O(n^2)
print(maxl)