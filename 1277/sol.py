class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cnt = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            cnt += matrix[i][0]
        for j in range(1, n):
            cnt += matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1], matrix[i][j-1]) + 1
                    cnt += matrix[i][j]
        return cnt