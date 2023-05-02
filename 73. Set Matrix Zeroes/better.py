matrix = [[1,1,1],[1,0,1],[1,1,1]]


row = [0 for i in range(len(matrix))]       #SC: O(n)
col = [0 for i in range(len(matrix[0]))]    #SC: O(m)   

for i in range(len(matrix)):
    for j in range(len(matrix[0])):         #TC: O(n*m)
        if matrix[i][j] == 0:
            row[i]=1
            col[j]=1
            

for j in range(len(matrix[0])):
    for i in range(len(matrix)):            #TC: O(n*m)
        if row[i]==1 or col[j]==1:
            matrix[i][j] = 0

# Total TC: O(2*n*m)
# Total SC: O(n) + O(m)

print(matrix)        

