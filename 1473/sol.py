class Solution(object):
    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """
        dp = [[[float("inf") for _ in range(n)] for _ in range(target+1)] for _ in range(m)]
        if houses[0] == 0:
            dp[0][1] = cost[0]
        else:
            for color in range(n):
                if color + 1 == houses[0]:
                    dp[0][1][color] = 0
        for i in range(1, m):
            if houses[i] == 0:
                for k in range(1, min(target, i + 1) + 1):
                    for c in range(n):
                        cost_ = cost[i][c]
                        for color in range(n):
                            if c == color:
                                dp[i][k][c] = min(dp[i][k][c], dp[i-1][k][color] + cost_)
                            else:
                                dp[i][k][c] = min(dp[i][k][c], dp[i-1][k-1][color] + cost_)
            else:
                for k in range(1, min(target, i + 1) + 1):
                    c = houses[i] - 1
                    for color in range(n):
                        if c == color:
                            dp[i][k][c] = min(dp[i][k][c], dp[i-1][k][color])
                        else:
                            dp[i][k][c] = min(dp[i][k][c], dp[i-1][k-1][color])
        res = min(dp[-1][-1])
        if res == float("inf"):
            return -1
        return res