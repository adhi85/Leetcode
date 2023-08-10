n = 4
k = 2

ans = []

def combination(cur,start):
    
    # If same length append to answer
    if len(cur) == k:
        ans.append(cur[:]) # cur.copy()
        return
    
    for i in range(start,n+1):
        cur.append(i)
        combination(cur,i+1)
        cur.pop()

combination([],1)
print(ans)