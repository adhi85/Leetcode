matrix =[[2, 6, 8],
[1 ,4, 7],
[6 ,8 ,9]]

nums = []

# TC: O(N*M)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        nums.append(matrix[i][j])

# O((N*M)log(N*M))
nums.sort()

print(nums[len(nums)//2])

# TC: O(N*M)log(N*M)
# SC: O(N*M)