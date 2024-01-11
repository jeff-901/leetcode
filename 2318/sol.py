class Solution(object):
    def distinctSequences(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 6
        d = {}
        d[0] = [1,2,3,4,5]
        d[1] = [0,2,4]
        d[2] = [0,1,3,4]
        d[3] = [0,2,4]
        d[4] = [0,1,2,3,5]
        d[5] = [0,4]
        dp = [[0, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 1, 0],
                [1, 1, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 0],
                [1, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 1, 0]]
        
        s = [5, 3, 4, 3, 5, 2]
        for _ in range(2, n):
            tmp = [[0 for _ in range(6)] for _ in range(6)]
            for i in range(6):
                for j in d[i]:
                    tmp[i][j] = s[j] - dp[j][i]
            for i in range(6):
                s[i] = sum(tmp[i]) % 1000000007
            dp = tmp
        return (sum(s)) % 1000000007