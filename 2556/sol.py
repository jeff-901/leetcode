class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        n = len(grid)
        m = len(grid[0])
        def dfs(r, c):
            if r == n - 1 and c == m -1: 
                return True
            grid[r][c] = 0
            if r + 1 < n and grid[r+1][c] == 1 and dfs(r+1, c):
                return True
            if c + 1 < m and grid[r][c+1] == 1 and dfs(r, c+1):
                return True
            return False
        if not dfs(0, 0):
            return True
        
        return not dfs(0, 0)
