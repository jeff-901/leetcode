class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        n = len(stoneValue)
        for i in range(n-2, -1, -1):
            stoneValue[i] += stoneValue[i+1]
        dp = [stoneValue[-1]]
        for i in range(2, min(3, n)+1):
            dp.insert(0, max(stoneValue[-i] - min(dp), stoneValue[-i]))
        for i in range(len(stoneValue)-4, -1, -1):
            val = stoneValue[i] - min(dp)
            dp.pop()
            dp.insert(0, val)
        if dp[0] * 2 > stoneValue[0]:
            return "Alice"
        elif dp[0] * 2 == stoneValue[0]:
            return "Tie"
        return "Bob"