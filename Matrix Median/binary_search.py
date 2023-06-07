def getCount(row,target):
    low = 0
    high = len(row) - 1

    while low <= high:
        md = (low + high) //2

        if row[md] <= target:
            low = md + 1
        else:
            high = md - 1

    return low

matrix =[[2, 6, 8],
[1 ,4, 7],
[6 ,8 ,9]]

rows = len(matrix)
columns = len(matrix[0])

min_el = matrix[0][0]
max_el = matrix[0][columns-1]

for i in range(rows):
    if matrix[i][0] < min_el:
        min_el = matrix[i][0]
    if matrix[i][columns - 1] > max_el:
        max_el = matrix[i][columns - 1]


while min_el <= max_el:
    mid = (min_el + max_el)//2

    count = 0

    for i in range(rows):
        count += getCount(matrix[i],mid)


    if count <= (rows * columns)//2 :
        min_el = mid + 1
    
    else :
        max_el = mid - 1

print(min_el)

# TC: O(N * log(max_el) * log(M)) == O(N) + O(log(max_el)) * N * O(log(M))  
# SC : O(!)