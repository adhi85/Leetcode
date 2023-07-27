class Solution:
    def nextGreaterElement(self, n: int) -> int:

        n = [*str(n)]
        dip = -1
        for i in range(len(n)-1, 0, -1):
            if int(n[i]) > int(n[i-1]):
                dip = i-1
                break

        if dip == -1:
            return -1

        for i in range(len(n)-1, dip, -1):
            if int(n[i]) > int(n[dip]):
                n[i], n[dip] = n[dip], n[i]
                break

        n[dip+1:] = n[:dip:-1]

        ans = int("".join(n))

        if ans > (2**31 - 1):
            return -1
        return ans
