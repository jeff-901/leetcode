class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], questions[i][0] + dp[min(n, i+questions[i][1]+1)])
        return dp[0]