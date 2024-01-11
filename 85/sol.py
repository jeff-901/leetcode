class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        m = len(matrix[0])
        grid = [0 for _ in range(m)]
        stack = []
        for row in range(len(matrix)):
            for col in range(m):
                if matrix[row][col] == "1":
                    grid[col] += 1
                else:
                    grid[col] = 0
                earliest = col
                while stack and grid[col] <= stack[-1][1]:
                    ans = max(ans, stack[-1][1] * (col - stack[-1][0]))
                    earliest, _ = stack.pop()
                stack.append([earliest, grid[col]])
            while stack:
                ans = max(ans, stack[-1][1] * (m - stack[-1][0]))
                stack.pop()
        return ans