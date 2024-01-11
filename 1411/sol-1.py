class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        state = ['010', '210', '020', '120', '101', '201', '021', '121', '102', '202', '012', '212']
        m = len(state)
        available = [[] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                flag = True
                for k in range(3):
                    if state[i][k] == state[j][k]:
                        flag = False
                        break
                if flag:
                    available[i].append(j)
        dp = [1 for _ in range(m)]
        for _ in range(1, n):
            new = [0] * m
            for i in range(m):
                for j in available[i]:
                    new[i] += dp[j]
                new[j] %= 1000000007
            dp = new
            print(dp)
        return sum(dp) % 1000000007

s = Solution()
s.numOfWays(5)