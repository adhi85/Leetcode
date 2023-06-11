def ninjaAndLadoos(row1, row2, m, n, k):
        i = j = 0
        ans = []

        while i<m and j <n:
            if row1[i] <= row2[j]:
                ans.append(row1[i])
                i+=1
            else:
                ans.append(row2[j])
                j+=1
        while i <m:
            ans.append(row1[i])
            i+=1
        while j <n:
            ans.append(row2[j])
            j+=1

        return ans[k-1]

# TC: O(m+n)
# SC: O(m+n)