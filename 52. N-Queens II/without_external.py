class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        
        board = [["."] * n for i in range(n)]
        
        
        def backtrack(r):
            if r == n:
                return 1
            
            ans = 0
            
            for c in range(n):
                if (c not in cols) and ((r+c) not in posDiag) and ((r-c)not in negDiag):
                    
                    cols.add(c)
                    posDiag.add((r+c))
                    negDiag.add((r-c))
                    
                    ans += backtrack(r+1)
                    
                    cols.remove(c)
                    posDiag.remove((r+c))
                    negDiag.remove((r-c))
            return ans
        
        return backtrack(0)
        
        
        