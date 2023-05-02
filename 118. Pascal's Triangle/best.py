def rowGen(numRows):
    ans =1.0
    main = []
    main.append(ans)
    for i in range(1,numRows):  #TC:O(n)
        ans = ans* (numRows-i)
        ans = ans / (i)
        main.append(ans)    

    return main
numRows = 5
fin = []
for i in range(1,numRows+1):   #TC:O(n)
    fin.append(rowGen(i))      #TC:O(n)

# Total TC:O(n^2)

print(fin)