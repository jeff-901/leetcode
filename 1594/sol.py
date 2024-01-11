class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        grid[0][0] = [grid[0][0], grid[0][0]]
        for j in range(1, n):
            product = grid[0][j] * grid[0][j-1][0]
            grid[0][j] = [product, product]
        for i in range(1, m):
            product = grid[i][0] * grid[i-1][0][0]
            grid[i][0] = [product, product]
        for i in range(1, m):
            for j in range(1, n):
                num = grid[i][j]
                if num < 0:
                    max_product = max(grid[i-1][j][1] * num, grid[i][j-1][1] * num)
                    min_product = min(grid[i-1][j][0] * num, grid[i][j-1][0] * num)
                    grid[i][j] = [max_product, min_product]
                elif num > 0:
                    max_product = max(grid[i-1][j][0] * num, grid[i][j-1][0] * num)
                    min_product = min(grid[i-1][j][1] * num, grid[i][j-1][1] * num)
                    grid[i][j] = [max_product, min_product]
                else:
                    grid[i][j] = [0, 0]
        ans = grid[-1][-1][0]
        if ans < 0:
            return -1 
        return ans % 1000000007