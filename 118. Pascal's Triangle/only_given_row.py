numRows = 5
ans =1
main = []
for i in range(5):
    main.append(ans)    
    ans = ans* (numRows-1-i)
    ans = ans / (i+1)

# Total TC:O(n)
print(main)