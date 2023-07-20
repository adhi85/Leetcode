nums = [1,2,3,4]
prefix = []
postfix = [0 for i in range(len(nums))]

x =1
for i in range(len(nums)):
    x *= nums[i]
    prefix.append(x)

x = 1
for i in range(len(nums)-1,-1,-1):
    x *= nums[i] 
    postfix[i] = x

ans = []
for i in range(len(nums)):
    if i == 0:
        ans.append(postfix[i+1])
    elif i == len(nums)-1:
        ans.append(prefix[i-1])
    else:
        ans.append(postfix[i+1] * prefix[i-1])

print(ans)