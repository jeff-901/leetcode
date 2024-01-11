class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_0 = -1
        last_1 = -1
        n = len(s)
        left_cost = [[0, 0] for _ in range(n+1)]
        for i in range(n):
            if s[i] == "1":
                left_cost[i+1][1] = left_cost[last_0+1][1]
                left_cost[i+1][0] = left_cost[last_0+1][1] + i + 1
                last_1 = i
            else:
                left_cost[i+1][0] = left_cost[last_1+1][0]
                left_cost[i+1][1] = left_cost[last_1+1][0] + i + 1
                last_0 = i
        last_0 = n
        last_1 = n
        right_cost = [[0, 0] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            if s[i] == "1":
                right_cost[i][1] = right_cost[last_0][1]
                right_cost[i][0] = right_cost[last_0][1] + (n-i)
                last_1 = i
            else:
                right_cost[i][0] = right_cost[last_1][0]
                right_cost[i][1] = right_cost[last_1][0] + (n-i)
                last_0 = i
        min_cost = float("inf")
        for i in range(n):
            min_cost = min(min_cost, left_cost[i+1][0] + right_cost[i][0], left_cost[i+1][1] + right_cost[i][1])
        return min_cost
