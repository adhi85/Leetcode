matrix = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]

var = 1
for i in range(len(matrix)):
    if matrix[i][0] == 0:
            var = 0
    for j in range(1,len(matrix[0])): #TC O(nm)
        if matrix[i][j] == 0:
            matrix[0][j]=0
            matrix[i][0]=0

for i in range(len(matrix)-1,0,-1):
    for j in range(len(matrix[0])-1,0,-1):  #TC O(nm)
        if matrix[i][0]==0 or matrix[0][j]==0:
            matrix[i][j]=0

if matrix[0][0] == 0:
    for i in range(len(matrix[0])-1,0,-1):
        matrix[0][j] = 0
if var==0 :
    for i in range(0,len(matrix)):
        matrix[i][0] = 0
    
# Total TC: O(2*n*m)
print(matrix) 

