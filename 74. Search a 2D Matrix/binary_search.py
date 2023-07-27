class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        l = 0
        row, col = len(matrix), len(matrix[0])
        r = (row*col) - 1

        while l <= r:

            mid = (l + r) // 2

            if matrix[mid//col][mid % col] == target:
                return True

            elif matrix[mid//col][mid % col] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False
