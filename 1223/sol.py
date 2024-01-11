class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(6)] for i in range(n)]
        dp[0] = [1] * 6
        total = [0 for i in range(n)]
        total[0] = 6
        for i in range(1, n):
            s = 0
            for dice in range(6):
                for j in range(rollMax[dice]):
                    if i > j:
                        dp[i][dice] += total[i-j-1] - dp[i-j-1][dice]
                    else:
                        dp[i][dice] += 1
                        break
                s += dp[i][dice]
            s = s % 1000000007
            total[i] = s
        # print(dp)
        # print(total)
        return sum(dp[-1]) % 1000000007