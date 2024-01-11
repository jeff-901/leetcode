class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        cnt = []
        n = len(words[0])
        t_set = set(target)
        for i in range(n):
            h = {}
            for word in words:
                if word[i] in t_set:
                    h[word[i]] = h.get(word[i], 0) + 1
            cnt.append(h)
        m = len(target)
        dp = [0 for _ in range(m+1)]
        dp[0] = 1
        for i in range(n - 1, -1, -1):
            for l in range(min(m, n-i), max(0, m-(i+1)-1), -1):
                dp[l] += dp[l-1] * cnt[i].get(target[-l], 0)
                dp[l] %= 1000000007
        return dp[-1] % 1000000007