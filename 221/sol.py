class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])
            ans = max(ans, matrix[0][j])
        for i in range(1, m):
            matrix[i][0] = int(matrix[i][0])
            ans = max(ans, matrix[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    ans = max(ans, matrix[i][j] ** 2)
                else:
                    matrix[i][j] = 0
        return ans