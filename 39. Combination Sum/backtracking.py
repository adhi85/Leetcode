candidates = [2,3,6,7]
target = 7

# TC: O(2^target)

ans = []

def dfs(i,cur,total):
    if total == target:
        ans.append(cur.copy())
        return
    
    if i >=len(candidates) or total>target:
        return
    
    cur.append(candidates[i])
    dfs(i,cur,total + candidates[i])

    cur.pop()
    dfs(i+1,cur,total)

dfs(0,[],0)

print(ans)