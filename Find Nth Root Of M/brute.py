def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    for i in range(1,m +1):
        k = 1
        for j in range(n):
            k *= i
        if k == m:
            return i
        elif k > m:
            break
    return -1 

print(NthRoot(4,16))

# TC: O(N*M)
# SC : O(1)