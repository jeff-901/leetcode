class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        m = len(pizza)
        n = len(pizza[0])
        mod = 10**9+7
        apples = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if pizza[i][j] == "A":
                    apples[i][j] = 1
        for i in range(m):
            for j in range(n-2, -1, -1):
                apples[i][j] += apples[i][j+1]
        for j in range(n):
            for i in range(m-2, -1, -1):
                apples[i][j] += apples[i+1][j]
        dp = [[int(apples[row][col] > 0) for col in range(n)] for row in range(m)]
        
        for remain in range(1, k):
            last = copy.deepcopy(dp)
            for row in range(m):
                for col in range(n):
                    dp[row][col] = 0
                    for next_row in range(row+1, m):
                        if apples[row][col] - apples[next_row][col] > 0:
                            dp[row][col] += last[next_row][col]
                    for next_col in range(col+1, n):
                        if apples[row][col] - apples[row][next_col] > 0:
                            dp[row][col] += last[row][next_col]
                dp[row][col] %= 1000000007
        # print(dp)
        return dp[0][0] % 1000000007