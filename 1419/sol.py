class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        dp = [0 for _ in range(4)]
        ans = 0
        cur = 0
        for c in croakOfFrogs:
            if c == "c":
                dp[0] += 1
                cur += 1
                ans = max(ans, cur)
            elif c == "r":
                if dp[0] == 0:
                    return -1
                dp[0] -= 1
                dp[1] += 1
            elif c == "o":
                if dp[1] == 0:
                    return -1
                dp[1] -= 1
                dp[2] += 1
            elif c == "a":
                if dp[2] == 0:
                    return -1
                dp[2] -= 1
                dp[3] += 1
            elif c == "k":
                if dp[3] == 0:
                    return -1
                dp[3] -= 1
                cur -= 1
        if cur > 0:
            return -1
        return ans