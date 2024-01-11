class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = grid[0][:]
        min_ele = [(20000, -1), (20000, -1)]
        for i, ele in enumerate(dp):
            if ele < min_ele[0][0]:
                min_ele[1] = min_ele[0]
                min_ele[0] = (ele, i)
            elif ele < min_ele[1][0]:
                min_ele[1] = (ele, i)
        for row in range(1, n):
            for i in range(n):
                if i != min_ele[0][1]:
                    dp[i] = min_ele[0][0] + grid[row][i]
                else:
                    dp[i] = min_ele[1][0] + grid[row][i]
            min_ele = [(20000, -1), (20000, -1)]
            for i, ele in enumerate(dp):
                if ele < min_ele[0][0]:
                    min_ele[1] = min_ele[0]
                    min_ele[0] = (ele, i)
                elif ele < min_ele[1][0]:
                    min_ele[1] = (ele, i)
        return min_ele[0][0]
