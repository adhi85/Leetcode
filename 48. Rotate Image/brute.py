matrix = [[1,2,3],[4,5,6],[7,8,9]]


n = len(matrix)

ans = [[0 for i in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        ans[j][n-1-i] = matrix[i][j]

# TC: O(n^2)
# SC: O(n^2)               
print(ans)