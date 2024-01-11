class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = [-1] + [len(s)] * 1023
        total = 0
        ans = 0
        for i in range(len(s)):
            total ^= 1 << int(s[i])
            for j in range(10):
                ans = max(ans, i - cnt[total ^ (1 << j)])
            ans = max(ans, i - cnt[total])
            cnt[total] = min(cnt[total], i)
        return ans