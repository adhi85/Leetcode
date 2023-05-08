intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
main = []

for i in range(len(intervals)):
    if(not main  or intervals[i][0] > main[-1][1]  ):
        main.append(intervals[i])
    else: 
        main[-1][1] = max(intervals[i][1], main[-1][1])

# TC : O(nlogn) + O(n)
# SC: O(n) 
print(main)