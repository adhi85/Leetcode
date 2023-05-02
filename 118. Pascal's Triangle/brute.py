# import math
# def nCr(i,j):
#     return math.factorial(i)/(math.factorial(j)*math.factorial(i-j))

def nCr(i,j):           #TC: O(j)
    k = 1
    for m in range(j):
        k = k * (i-m)
        k = k/(m+1)
    return k
numRows = 5

temp = []
main = []

for i in range(numRows):   #TC: O(i)
    for j in range(i+1):   #TC: O(i)
        if(j>(i/2)):
            temp.append(nCr(i,i-j))
        else:
            temp.append(nCr(i,j))
    main.append(temp)
    temp = []

# Total TC: O(i*i*j) almost O(n^3)

print(main)