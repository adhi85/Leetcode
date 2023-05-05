nums = [5,4,-1,7,8]

main = []

for i in range(len(nums)): #TC: O(n)
    for j in range(i+1,len(nums)+1):   #TC: O(n)
        main.append(list(nums[i:j]))    #TC: O(n)
maxl = min(nums)
for i in range(len(main)):     
    sm = sum(main[i])
    if(sm>maxl):
        maxl = sm
#Total TC: O(n^3)  approximately
# Total SC: O(m)
print(maxl)


