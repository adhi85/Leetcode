arr = [2 ,5 ,1 ,3 ,4]
c =0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            c+=1
print(c)

# TC: O(n^2)