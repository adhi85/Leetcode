import math
def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here

    low = 1
    high = m

    while low <= high:
        mid = (low+high) //2

        k = 1
        for i in range(n):
            k *= mid
        if k == m:
            return mid
        elif k > m:
            high = mid-1
        else:
            low = mid + 1
    return -1

