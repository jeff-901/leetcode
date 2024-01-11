class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [[] for _ in range(len(s) + 1)]
        dp[0].append("")
        n = len(s)
        wordDict = set(wordDict)
        for i in range(1, n + 1):
            if s[:i] in wordDict:
                dp[i].append(s[:i])
            for j in range(1, i):
                if dp[j] and s[j:i] in wordDict:
                    for ele in dp[j]:
                        dp[i].append(ele + " " + s[j:i])
        return dp[-1]
