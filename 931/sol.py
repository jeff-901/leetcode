class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = matrix[0][:]
        for row in range(1, m):
            last = 100000
            for col in range(n-1):
                tmp = dp[col]
                dp[col] = min([last]+dp[col:col+2]) + matrix[row][col]
                last = tmp
            dp[n-1] = min(dp[n-1], last) + matrix[row][n-1]
        return min(dp)