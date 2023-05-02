matrix = [[1,1,1],[1,0,1],[1,1,1]]


row = [0 for i in range(len(matrix))]
col = [0 for i in range(len(matrix[0]))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            row[i]=1
            col[j]=1
            

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        if row[i]==1 or col[j]==1:
            matrix[i][j] = 0

print(matrix)            
