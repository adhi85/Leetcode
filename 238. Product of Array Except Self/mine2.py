nums = [1,2,3,4]

def multiply(arr):
    x = 1
    for i in range(len(arr)):
        x *= arr[i]
    return x

ans = []

for i in range(len(nums)-1):
    pre = multiply(nums[:i])
    post = multiply(nums[i+1:])
    
    ans.append(pre*post)

ans.append(multiply(nums[:i+1]))
    
print(ans)