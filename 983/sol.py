class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(3)] for _ in range(366)]
        day_idx = 0
        for day in range(1, days[-1]+1):
            if days[day_idx] == day:
                day_idx += 1
                dp[day][0] = min(dp[day - 1]) + costs[0]
                dp[day][1] = (min(dp[day-7]) if day - 7 > -1 else 0) + costs[1]
                dp[day][2] = (min(dp[day-30]) if day - 30 > -1 else 0) + costs[2]
            else:
                for i in range(3):
                    dp[day][i] = dp[day-1][i]
        return min(dp[days[-1]])