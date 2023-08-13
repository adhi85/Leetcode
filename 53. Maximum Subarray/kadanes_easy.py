nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Kadanes algo

maxi = float("-inf")

summ = 0

for i in range(len(nums)):

    # To print the maximum sum subarray => Every starting the summ is 0.
    if summ == 0: start = i

    # Adding the elements
    summ += nums[i]
    # Taking maximum
    if summ>maxi:
        maxi = summ
        # TO print the maximum sum subarray => i will go up but make ansStart as start
        ansStart = start
        ansEnd = i

    # If negative make summ 0 since no point in carrying negative summ
    if summ < 0:
        summ = 0

print(maxi)
print(nums[ansStart:ansEnd+1])
