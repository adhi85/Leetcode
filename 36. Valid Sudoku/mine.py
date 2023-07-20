class Solution:
    def isValidSudoku(self, board):
        
        def box(brd,r,c):
            bo = [0 for i in range(10)]

            for i in range(r,r+3,1):
                for j in range(c,c+3,1):
                    try:
                        bo[int(brd[i][j])] +=1
                    except:
                        pass
            for i in range(10):
                if bo[i] > 1:
                    return -1
            return 1
        
        for i in range(9):
            row = [0 for i in range(10)]
            for j in range(9):
                try:
                    row[int(board[i][j])]+=1
                except:
                    pass
            
            for j in range(10):
                if row[j] > 1:
                    return False
                
        for i in range(9):
            col = [0 for i in range(10)]
            for j in range(9):
                try:
                    col[int(board[j][i])] +=1
                except:
                    pass
            
            for j in range(10):
                if col[j] > 1:
                    return False
                
        for i in range(0,9,3):
            for j in range(0,9,3):
                x = box(board,i,j)
                if x == -1:
                    return False
        
        return True
                