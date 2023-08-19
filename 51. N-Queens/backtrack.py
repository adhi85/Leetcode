class Solution:
    def solveNQueens(self, n: int):

        cols = set()
        posDiag = set()  # r+c
        negDiag = set()  # r-c

        ans = []

        board = [["."] * n for i in range(n)]

        def backtrack(r):

            if r == n:
                temp = ["".join(row) for row in board]
                ans.append(temp)
                return

            for c in range(n):

                if (c not in cols) and ((r-c)not in negDiag) and ((r+c) not in posDiag):

                    board[r][c] = "Q"
                    cols.add(c)
                    negDiag.add((r-c))
                    posDiag.add((r+c))

                    backtrack(r+1)

                    board[r][c] = "."
                    cols.remove(c)
                    negDiag.remove((r-c))
                    posDiag.remove((r+c))
        backtrack(0)
        return ans
