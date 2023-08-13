candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

candidates.sort()

ans = []

def backtrack(index,curr,target):
    
    if  target == 0:
        ans.append(curr[::])
        return
    
    if target <0: return

    prev = -1

    for i in range(index,len(candidates)):
        if candidates[i] == prev:
            continue
        curr.append(candidates[i])
        backtrack(i+1,curr,target-candidates[i])
        curr.pop()
        prev = candidates[i]

backtrack(0,[],target)
print(ans)