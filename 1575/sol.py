class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        if abs(locations[finish]-locations[start]) > fuel:
            return 0
        dp=[[-1 for _ in range(fuel+1)]for _ in range(len(locations))]
        def dfs(cur, cost):
            if cost < 0:
                return 0
            if dp[cur][cost] != -1:
                return dp[cur][cost]
            ans = int(cur == finish)
            if abs(locations[cur] - locations[finish]) > cost:
                dp[cur][cost] = 0
                return 0
            for i, ele in enumerate(locations):
                if i != cur:
                    ans += dfs(i, cost - abs(ele-locations[cur]))
            dp[cur][cost] = ans
            return ans
        return dfs(start,fuel) % 1000000007
