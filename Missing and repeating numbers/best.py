nums = [3,1,2,5,3] 
n = len(nums)
nums_sum = sum(nums)

nums_sq_sum = 0

for i in range(len(nums)):
    nums_sq_sum += nums[i]**2


real_sum = n * (n+1) // 2

real_sq_sum = n * (n+1) * ((2*n)+1) // 6  

x_minus_y = real_sum - nums_sum

x_pls_y = (real_sq_sum-nums_sq_sum) // x_minus_y

# x is missing value 
x = (x_minus_y + x_pls_y) //2
# y is repeating value 
y = x_pls_y - x

print(x)
print(y)
 


    

    
    