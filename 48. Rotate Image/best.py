matrix = [[1,2,3],[4,5,6],[7,8,9]]


n = len(matrix)

#TRanspose the matrix
for i in range(n):
    for j in range(i):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

# Reverse Every row
for i in matrix:
    i.reverse()
    
print(matrix)