def ninjaAndLadoos(row1, row2, m, n, k):
    # Write your code here.

    if m > n:
        ninjaAndLadoos(row2,row1,n,m,k)

    low = max(0,k-n)
    high =min(k,m)


    while low<= high:
        cut1 = (low+high) >> 1

        cut2 = k-cut1

        l1 = 0 if cut1 ==0 else row1[cut1-1] 
        l2 = 0 if cut2 ==0 else row2[cut2-1]

        r1 = 10**5 if cut1 == m else row1[cut1]
        r2 = 10**5 if cut2 == n else row2[cut2]

        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1

# TC: O(log(min(m,n)))
# SC: O(1)