class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        posDiag = set()  # r+c
        negDiag = set()  # r-c

        ans = 0

        def backtrack(r):
            nonlocal ans

            if r == n:
                ans += 1
                return

            for c in range(n):
                if (c not in cols) and ((r+c) not in posDiag) and ((r-c)not in negDiag):

                    cols.add(c)
                    posDiag.add((r+c))
                    negDiag.add((r-c))

                    backtrack(r+1)

                    cols.remove(c)
                    posDiag.remove((r+c))
                    negDiag.remove((r-c))

        backtrack(0)
        return ans
