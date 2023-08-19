class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        
        board = [["."] * n for i in range(n)]
        
        ans = [0]
        maxA = [0]
        
        def backtrack(r):
            if r == n:
                ans[0] +=1
                maxA[0] = max(maxA[0], ans[0])    
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
        
        
        return maxA[0]