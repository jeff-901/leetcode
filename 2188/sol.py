class Solution(object):
    def minimumFinishTime(self, tires, changeTime, numLaps):
        """
        :type tires: List[List[int]]
        :type changeTime: int
        :type numLaps: int
        :rtype: int
        """
        tires.sort()
        min_r = tires[0][1]
        new_tires = [tires[0]]
        for i in range(1, len(tires)):
            if tires[i][1] < min_r:
                new_tires.append(tires[i])
                min_r = tires[i][1]
        n = len(new_tires)
        tires = new_tires
        dp = [[0 for _ in range(numLaps+1)] for _ in range(n)]
        f, r = tires[0]
        vals = [0]
        for l in range(1, numLaps+1):
            vals.append(f * (r ** (l - 1)))
            vals[-1] += vals[-2]
        for i in range(1, numLaps+1):
            dp[0][i] = vals[i]
            for l in range(1, min(i//2+1, 19)):
                dp[0][i] = min(dp[0][i], dp[0][i-l] + vals[l] + changeTime)
        for i in range(1, n):
            f, r = tires[i]
            vals = [0]
            for l in range(1, min(numLaps+1, 19)):
                vals.append(f * (r ** (l - 1)))
                vals[-1] += vals[-2]
            for j in range(1, numLaps + 1):
                if j < 19:
                    dp[i][j] = min(dp[i-1][j], vals[j])
                else:
                    dp[i][j] = dp[i-1][j]
                for l in range(1, min(j, 19)):
                    dp[i][j] = min(dp[i][j], dp[i][j-l] + vals[l] + changeTime)
        return dp[-1][-1]