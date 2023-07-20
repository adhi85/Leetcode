def multiply(arr):
    x = 1
    for i in range(len(arr)):
        x *= arr[i]
    
    return x
nums = [1,2,3,4]
ans = []
for i in range(len(nums)):
    a = nums[i]
    
    nums.pop(i)
    
    val = multiply(nums)
    
    nums.insert(i,a)
    
    ans.append(val)
    
print(ans)