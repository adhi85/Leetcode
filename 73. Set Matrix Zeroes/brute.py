def markRow(i,matrix):
    for k in range(len(matrix[0])):
        if matrix[i][k] != 0 :
            matrix[i][k] = -1
def markCol(j,matrix):
    for i in range(len(matrix)):
        if matrix[i][j] !=0:
            matrix[i][j] = -1
    

matrix = [[0,1]]


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            markRow(i,matrix)
            markCol(j,matrix)
            
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == -1:
            matrix[i][j] = 0
            
print(matrix)
            
