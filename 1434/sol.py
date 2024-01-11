class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        people = [[] for _ in range(40)]
        n = len(hats)
        for i in range(n):
            for hat in hats[i]:
                people[hat-1].append(i)
        bitmask = 2 ** n
        dp = [0 for _ in range(bitmask)]
        dp[0] = 1
        for hat in range(40):
            last = dp[:]
            for p in people[hat]:
                bit = 1 << p
                for i in range(bitmask):
                    if bit & i == 0:
                        dp[bit ^ i] = (dp[bit ^ i] + last[i]) % 1000000007
        return dp[-1]