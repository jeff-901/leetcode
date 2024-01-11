class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        c2pos = {}
        for i, ele in enumerate(ring):
            if ele in c2pos:
                c2pos[ele].append(i)
            else:
                c2pos[ele] = [i]
        m = len(ring)
        n = len(key)
        dp = [{} for _ in range(n)]
        for pos in c2pos[key[0]]:
            dp[0][pos] = min(pos, m - pos) + 1
        for i in range(1, n):
            for des in c2pos[key[i]]:
                ans = float("inf")
                for last_pos in dp[i-1]:
                    diff = abs(last_pos-des)
                    ans = min(ans, dp[i-1][last_pos] + min(diff, m - diff) + 1)
                dp[i][des] = ans
        return min(dp[-1].values())