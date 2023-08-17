class Solution:
    def exist(self, board, word):

        # TC: O(n * m) * 4^ len(word)

        rows = len(board)
        cols = len(board[0])

        path = set()

        def dfs(r, c, i):

            if len(word) == i:
                return True

            if (r >= rows or c >= cols or
                r < 0 or c < 0 or
                board[r][c] != word[i] or
                    (r, c) in path):

                return False

            path.add((r, c))

            res = (dfs(r + 1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c-1, i+1))

            path.remove((r, c))

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
