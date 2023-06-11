def ninjaAndLadoos(row1, row2, m, n, k):
    i = j  = 0
    elem = 1
    while i<m and j<n:
        if row1[i] <= row2[j]:
            if elem ==k:
                return row1[i]
            i+=1
            elem+=1
        else:
            if elem ==k:
                return row2[j]
            j+=1
            elem+=1
    while i<m:
        if elem == k:
            return row1[i]
        i+=1
        elem+=1          
    while j<n:
        if elem == k:
            return row2[j]
        j+=1
        elem+=1    

    # TC:O(k)  
    # SC:O(1)


    