intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
main = []

for i in range(len(intervals)):
    start = intervals[i][0]
    end = intervals[i][1]
    
    if (len(main)!=0 and end <= main[-1][1] ):
        continue
    
    for j in range(i+1,len(intervals)):
        if(intervals[j][0] <= end):
            end = max(end,intervals[j][1])
        else:
            break
    main.append([start,end])
    
#      Sort    + Loop 
# TC: O(nlogn) + O(2*n)
print(main)